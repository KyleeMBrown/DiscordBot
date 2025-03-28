import discord
from discord.ext import commands

# on server join
class Intro(commands.Cog):  # Using commands.Cog even though you have only event listeners
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        print(f"Joined a new server: {guild.name}")
        jarvisIntroText = discord.Embed(
            title="Hi I'm JarvisRivals!",
                description='''I am your **Marvel Rivals** Companion here to make
                your experience better:\n
                **I can...**
                \nGet character summaries:
                   > • Just send a message like *"Mantis Information"*
                   > • Or use shortcut like "iw" for invisible woman or "cd" for cloak and dagger
                \nAssemble a team through Jarvis AI:
                    > • just send a message like *"Jarvis assemble a marval rivals team"*
                \n Please Enjoy!
                \n ~ Developers
                  ''',
                color=discord.Color.red()
        )
        
        if guild.system_channel:
            await guild.system_channel.send(embed=jarvisIntroText)
# Setup the cog
async def setup(bot):
    await bot.add_cog(Intro(bot))

    '''  just send a message like
                    > "Mantis Information"

                '''