from Import_file import *

class economy_system(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def coin_message(self, coins):
        coins = 5
        return coins

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author.bot:
            return

        if message.content.startswith("?"):
            return
            
        guild_id = str(message.guild.id)
        user_id = str(message.author.id)
        guild_name = message.guild.name
        user_name = message.author.name
            
        check_econemy = "SELECT * FROM "
        check_econemy_values = []

def setup(bot):
    bot.add_cog(economy_system(bot))
   
