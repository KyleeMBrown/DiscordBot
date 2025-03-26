import discord
from discord.ext import commands
import json

#import data file
with open('cogs/characterData.json', 'r') as file:
    data = json.load(file)

# on server join
class CharacterInfo(commands.Cog):  # Using commands.Cog even though you have only event listeners
    def __init__(self, bot):
        self.bot = bot

    # if user types [character] + info
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        orig_str = message.content
        user_str = orig_str.replace("&", "and").lower()
        

        for character in data:
            if (character["name"].lower() in user_str and "info" in user_str) or orig_str.lower() in character["shortcuts"]:
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
                user = message.author
                await message.channel.send(f'Here is some info on **{character["name"]}** {user.mention}!' )
                await message.channel.send(embed=characterCard )

async def setup(bot):
    await bot.add_cog(CharacterInfo(bot))     