import discord
from discord.ext import commands
import os
from flask import Flask
from threading import Thread

app = Flask('')


@app.route('/')
def home():
    return "Hello, I'm alive!"


def run():
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()


# Get the bot token from environment variables
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

# Define the bot's intents
intents = discord.Intents.default()
intents.message_content = True  # Ensure the bot can read message content

# Define the bot's command prefix and intents
bot = commands.Bot(command_prefix='!', intents=intents)


# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')


# Command: Ping
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')


# Start the web server
keep_alive()

# Run the bot
bot.run(TOKEN)

# Make sure to replace 'DISCORD_BOT_TOKEN' with your actual Discord bot token or set it as an environment variable in Replit using the Secrets feature.
# use any uptime bot to this replit code.

## MERCENARY ONE