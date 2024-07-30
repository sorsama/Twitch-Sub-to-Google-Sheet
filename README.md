
# Twitch to Google Sheets Integration
![Google Sheet](https://cdn.discordapp.com/attachments/897680966707974144/1267815315111415902/48501baec5bef51b.png?ex=66aa2885&is=66a8d705&hm=53811dd1de65960f449dd1d760bf7a370be32404d646628e25023bb732b73924&)
  

## Overview

  

Automates the process of listing Twitch subscribers and their subscription tiers in a Google Sheet. It fetches subscriber data from the Twitch API and updates a specified Google Sheet every seconds.

  

## Features

  

- Fetches Twitch subscribers' data using Twitch API.

- Updates Google Sheets with subscriber names and their subscription tiers every seconds.
  

## Requirements

  

- Python 3.6 or higher

-  `python-dotenv` for loading environment variables

-  `requests` for making HTTP requests to the Twitch API

-  `gspread` for interacting with Google Sheets

- A Twitch developer account and Google Sheets API credentials

  

## Setup

  

### 1. Install Dependencies

  

Install the required Python packages using pip:

  

```bash
pip  install  python-dotenv  requests  gspread  google-auth
```
  

### 2. Create a .env File

Create a .env file in the root directory of the project and add your Twitch and Google Sheets credentials:
```env
TWITCH_CLIENT_ID  =  'https://twitchtokengenerator.com/'
TWITCH_ACCESS_TOKEN  =  'https://twitchtokengenerator.com/'
TWITCH_USER_ID  =  'https://www.streamweasels.com/tools/convert-twitch-username-to-user-id/'
GOOGLE_SHEET_ID  =  'On URL of your sheet'
GOOGLE_CREDENTIALS  =  'https://console.cloud.google.com/iam-admin/serviceaccounts'
```
### 3. Google Sheets API Setup

1.  Go to the [Google Developers Console](https://console.cloud.google.com).
2.  Create a new project or select an existing one.
3.  Enable the Google Sheets API.
4.  Create Service Account credentials and download the JSON file.
5.  Share your Google Sheet with the service account email address found in the JSON file.

### 4. Run the Script

To start the script, run:
```bash
python ToSheet.py
```

## Contributing

Please open an issue or submit a pull request if you have suggestions or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](https://raw.githubusercontent.com/sorsama/Twitch-Sub-to-Google-Sheet/main/LICENSE) file for details.

[![https://www.twitch.tv/soursama_](https://cdn.discordapp.com/attachments/897680966707974144/1267815565670486171/ayaya256.png?ex=66aa28c1&is=66a8d741&hm=6bd02f70f3d117e6c69c50d61bad86115b9fb286c154c0ff1749dbaed91da11f&)](https://www.twitch.tv/soursama_)
