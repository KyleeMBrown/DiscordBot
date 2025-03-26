import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from google import genai

load_dotenv()

KEY = os.getenv("AI_KEY")
# Create open API client

client = genai.Client(api_key=KEY)

# on server join
class JarvisAI(commands.Cog):  # Using commands.Cog even though you have only event listeners
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
        content = orig_str.lower().replace("jarvis", "")
        
        if orig_str.lower().startswith("jarvis"):
            response = client.models.generate_content(
            model="gemini-2.0-flash", contents=f"{content} in 2000 characters or less"
            )
            #print(response.text)
            #print(content)
            responseEmbed = discord.Embed(
                title="Response",
                description=f"{response.text}"
            )
            await message.channel.send(embed=responseEmbed)
# cog setup
async def setup(bot):
    await bot.add_cog(JarvisAI(bot))     