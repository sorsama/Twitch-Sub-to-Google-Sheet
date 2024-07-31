import os
import time
from dotenv import load_dotenv
import requests
from google.oauth2.service_account import Credentials
import gspread

load_dotenv()

# Config timer
SLEEP_TIME = 10

# Twitch API
TWITCH_CLIENT_ID = os.getenv('TWITCH_CLIENT_ID')
TWITCH_ACCESS_TOKEN = os.getenv('TWITCH_ACCESS_TOKEN')
TWITCH_USER_ID = os.getenv('TWITCH_USER_ID')

# Google Sheets API 
GOOGLE_SHEET_ID = os.getenv('GOOGLE_SHEET_ID', '1Z4k0n3d5wiqlANmMtCj12nnFMVmox_EqS7xJsiOF_OE')
GOOGLE_CREDENTIALS = os.getenv('GOOGLE_CREDENTIALS', 'tosheet-431011-7b8a4669cd87.json')
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# Why Twitch make subtiers numberic? IDK LOL 
TIER_NAMES = {
    '1000': 'Tier 1',
    '2000': 'Tier 2',
    '3000': 'Tier 3'
}

print("Starting...")
print("Data fetch every: ", SLEEP_TIME, "sec")

# Function to get Twitch subscribers
def get_twitch_subscribers():
    url = f'https://api.twitch.tv/helix/subscriptions?broadcaster_id={TWITCH_USER_ID}'
    headers = {
        'Client-ID': TWITCH_CLIENT_ID,
        'Authorization': f'Bearer {TWITCH_ACCESS_TOKEN}'
    }
    response = requests.get(url, headers=headers)
    data = response.json()

    
    # Debugging: Print out the full response
    # print(data)
    
    if response.status_code != 200:
        print(f"Error: {data.get('message', 'Unknown error')}")
        return None
    
    return data

# Function to add or update data in Google Sheets
def add_to_google_sheet(data):
    if not data or 'data' not in data:
        print("No valid data to add to Google Sheets.")
        return
    
    credentials = Credentials.from_service_account_file(GOOGLE_CREDENTIALS, scopes=SCOPES)
    client = gspread.authorize(credentials)
    sheet = client.open_by_key(GOOGLE_SHEET_ID).sheet1
    
    # Fetch existing data
    existing_data = sheet.get_all_values()
    existing_users = {row[0]: row[1] for row in existing_data[1:]}  # Skip the header row

    for subscriber in data['data']:
        user_name = subscriber.get('user_name', 'Unknown')
        tier_value = subscriber.get('tier', 'Unknown')
        tier_name = TIER_NAMES.get(tier_value, 'Unknown Tier')

        # Check if the subscriber exists and if the tier is the same
        if user_name in existing_users:
            # If the tier is different, update the record
            if existing_users[user_name] != tier_name:
                row_number = list(existing_users.keys()).index(user_name) + 2  # +2 for 1-based index and header row
                sheet.update_cell(row_number, 2, tier_name)
                print(f"Updated {user_name}'s tier to {tier_name}.")
        else:
            # Add new subscriber only if not already present
            sheet.append_row([user_name, tier_name])
            print(f"Added new subscriber: {user_name}, {tier_name}.")

# Main function to run periodically
def main():
    while True:
        subscribers = get_twitch_subscribers()
        if subscribers:
            add_to_google_sheet(subscribers)
        else:
            print("No subscribers data retrieved.")
        
        # Wait for 10 sec
        time.sleep(SLEEP_TIME)

if __name__ == "__main__":
    main()