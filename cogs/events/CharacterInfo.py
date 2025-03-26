import discord
from discord.ext import commands
import json

#import data file
with open('cogs/characterData.json', 'r') as file:
    data = json.load(file)

# on server join
class CharacterInfo(commands.Cog):  # Using commands.Cog even though you have only event listeners
    # initialize bot
    def __init__(self, bot):
        self.bot = bot

    # send character info after user prompts 
    @commands.Cog.listener()
    async def on_message(self, message):
        # if bot is messaging do not respond
        if message.author == self.bot.user:
            return
        # grab message content
        orig_str = message.content
        # replace and lowercase the string to match data
        user_str = orig_str.replace("&", "and").lower()
        
        # iterate through data
        for character in data:
            #if user types [character] + info or a shortcut
            if (character["name"].lower() in user_str and "info" in user_str) or orig_str.lower() in character["shortcuts"]:
                # character card
                characterCard = discord.Embed(
                    title=character["name"],
                    description=f'''           
                    Role: {character['role']}\n
                    Pick Rate: {character['pickRate']}%
                    Win Rate: {character['winRate']}%
                    ''',
                    color=discord.Color.dark_gold()
                )
                characterCard.set_thumbnail(url=character['url'])
                # stor author as user
                user = message.author
                # send info
                await message.channel.send(f'Here is some info on **{character["name"]}** {user.mention}!' )
                await message.channel.send(embed=characterCard )
# cog setup
async def setup(bot):
    await bot.add_cog(CharacterInfo(bot))     