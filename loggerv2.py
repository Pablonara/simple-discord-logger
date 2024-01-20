import discord
from discord.ext import commands

intents = discord.Intents.all()


LOG_CHANNEL_ID = 123

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    channel = bot.get_channel(LOG_CHANNEL_ID)
    if channel:
        print(f"Logging deletions in channel: {channel.name}")
    else:
        print(f"Could not find the specified channel with ID: {LOG_CHANNEL_ID}")

@bot.event
async def on_message_delete(message):
    # Check if the message is not from the bot itself and not from the log channel
    if message.author != bot.user: # and message.channel.id != LOG_CHANNEL_ID:
        content = f"Message deleted from {message.author}: {message.content}"

        for attachment in message.attachments:
            content += f"\nImage from {message.author}: {attachment.url}"

        log_channel = bot.get_channel(LOG_CHANNEL_ID)
        if log_channel:
            await log_channel.send(content)
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True  # 
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

bot.run("YOUR_SECRET_KEY")
