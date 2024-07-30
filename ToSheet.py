import os
import time
from dotenv import load_dotenv
import requests
from google.oauth2.service_account import Credentials
import gspread

load_dotenv()

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
    print(data)
    
    if response.status_code != 200:
        print(f"Error: {data.get('message', 'Unknown error')}")
        return None
    
    return data

# Function to add data to Google Sheets
def add_to_google_sheet(data):
    if not data or 'data' not in data:
        print("No valid data to add to Google Sheets.")
        return
    
    credentials = Credentials.from_service_account_file(GOOGLE_CREDENTIALS, scopes=SCOPES)
    client = gspread.authorize(credentials)
    sheet = client.open_by_key(GOOGLE_SHEET_ID).sheet1
    
    # Clear existing data (optional, to avoid duplicates)
    sheet.clear()
    
    for subscriber in data['data']:
        user_name = subscriber.get('user_name', 'Unknown')
        tier_value = subscriber.get('tier', 'Unknown')
        tier_name = TIER_NAMES.get(tier_value, 'Unknown Tier')
        sheet.append_row([user_name, tier_name])

# Main function to run periodically
def main():
    while True:
        subscribers = get_twitch_subscribers()
        if subscribers:
            add_to_google_sheet(subscribers)
        else:
            print("No subscribers data retrieved.")
        
        # Wait for 10 seconds before checking again[Twitch limit at 30/mins] (adjust as needed)
        time.sleep(10)

if __name__ == "__main__":
    main()