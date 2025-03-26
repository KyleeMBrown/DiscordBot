from dotenv import load_dotenv
import os
import discord
from discord.ext import commands

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True


TOKEN = os.getenv("TOKEN")

#client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix="!", intents=intents)
cogs = ["events.JarvisIntro", "events.CharacterInfo"]
async def load_cogs():
    for cog in cogs:
        await bot.load_extension(f"cogs.{cog}")
        

@bot.event
async def on_ready():
    await load_cogs()
    print(f'We have logged in as {bot.user}')
    


if __name__ == "__main__":
    bot.run(TOKEN)
