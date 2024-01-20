# simple-discord-logger
Simple discord bot to log deleted messages. Attachments included.

### Requirements
- python
- discord.py (install with pip install discord.py)

## Setup

1. Install discord.py
2. Download loggerv2.py
   
### Creating a new bot
1. Go to https://discord.com/developers/applications and press the 'New Application' Button on the top right
2. Give it a name and create the application
3. (Optional) Once created, go to your application and the bot tab, and change the name and profile picture of the bot

### Getting the channel id for logged messages and your secret key
1. Enable developer mode in discord
2. Go to your server, and right click the channel you want logged messages to be in. Press copy channel id
3. Replace your copied channel id with the value after LOG_CHANNEL_ID in loggerv2.py.
4. Go to the the discord developer portal -> applications -> oauth2 and get your client secret key there.
5. Replace YOUR_SECRET_KEY in loggerv2.py with your key.

### Inviting your bot to your server
1. Go to oauth2 -> Url Generator in the discord developer portal.
2. Press 'bot' under scopes.
3. Check 'Read Messages/View Channels', 'Send Messages', 'Read Message History', 'Use External Emojis', and 'Use External Stickers'.
4. Copy the url generated underneath and paste it into your browser of choice. You will now have a prompt to invite your bot to a server.

### Running the script
Open command prompt and navigate to your directory where loggerv2.py is downloaded. Type python3 loggerv2.py and press enter.
