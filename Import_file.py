import asyncio
import random
import os
import json
import discord.ext
from discord.ext.commands import MissingPermissions
import discord
from discord.ext import commands, tasks
import mysql.connector
from datetime import *
import requests
from giphy_client.rest import ApiException
from discord.ui import *
from discord.commands import Option
from PIL import Image


"""
┏━━━┓ ┏━━━┓ ┏┓ ┏┓ ┏━━┓ ┏━━━┓ ┏━━┓
┃┏━┓┃ ┃┏━┓┃ ┃┃ ┃┃ ┗┫┣┛ ┗┓┏┓┃ ┗┫┣┛
┃┗━━┓ ┃┃ ┃┃ ┃┃ ┃┃  ┃┃   ┃┃┃┃  ┃┃
┗━━┓┃ ┃┗━┛┃ ┃┃ ┃┃  ┃┃   ┃┃┃┃  ┃┃
┃┗━┛┃ ┗━━┓┃ ┃┗━┛┃ ┏┫┣┓ ┏┛┗┛┃ ┏┫┣┓
┗━━━┛    ┗┛ ┗━━━┛ ┗━━┛ ┗━━━┛ ┗━━┛
"""

class setup_control(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    def set_prefix_connect(self):
        setup_connector = mysql.connector.connect(host='localhost', user='root', password=os.getenv("sql_passwort"), database='setup')
        return setup_connector
    


    @commands.Cog.listener()
    async def on_guild_join(self, guild):

        setup_db = self.set_prefix_connect()
        my_cursor = setup_db.cursor()

        standard_prefix = "?"
        guild_id_setup = str(guild.id)

        join_guild_check = f"SELECT * FROM slash_command_setup WHERE guild_id = %s"
        join_guild_check_values = [guild_id_setup]
        my_cursor.execute(join_guild_check, join_guild_check_values)

        all_guild_ids = my_cursor.fetchall()
        
        guild_ids = []
        for all_guild_ids in all_guild_ids:
            guild_id_user = all_guild_ids[0]
            
            guild_ids.append(guild_id_user)

        if guild_id_setup == all_guild_ids[0]:
            return
        
        else:
            
            try:

                sql_insert_setup_guild = "INSERT INTO slash_command_setup (guild_id, prefix) VALUES (%s, %s)"
                setup_guild_values = [guild_id_setup, standard_prefix]

                my_cursor.execute(sql_insert_setup_guild, setup_guild_values)
                setup_db.commit()

            except mysql.connector.Error as error:
                print("parameterized query failed {}".format(error))

            finally:

                if setup_db.is_connected():
                
                    my_cursor.close()
                    setup_db.close()

                else:
                    pass
    


    @commands.Cog.listener()
    async def on_guild_remove(self, guild):

        setup_db = self.set_prefix_connect()
        my_cursor = setup_db.cursor()

        remove_guild_setup = str(guild.id)

        remove_guild_check = f"SELECT * FROM slash_command_setup WHERE guild_id = %s"
        remove_guild_check_values = [remove_guild_setup]

        my_cursor.execute(remove_guild_check, remove_guild_check_values)
    	
        all_guild = my_cursor.fetchall()

        if all_guild:
            
            if remove_guild_setup in all_guild[0]:
                
                try:

                    sql_insert_setup_guild = "DELETE FROM slash_command_setup WHERE guild_id = %s"
                    setup_guild_values = [remove_guild_setup]

                    my_cursor.execute(sql_insert_setup_guild, setup_guild_values)
                    setup_db.commit()

                except mysql.connector.Error as error:
                    print("parameterized query failed {}".format(error))

                finally:

                    if setup_db.is_connected():
                    
                        my_cursor.close()
                        setup_db.close()
                        
                    else:
                        pass
            
            else:
                pass

        else:
            pass
    

    # Übersetzen 
    @commands.slash_command(name = "set-prefix", description = "Wähle einen eigenen individuellen prefix für deinen server!")
    @commands.has_permissions(administrator=True)
    async def set_prefix_slash(self,ctx , prefixe:Option(str, description="Gib deinen Prefix ein!")):

        setup_db = self.set_prefix_connect()
        my_cursor = setup_db.cursor()

        set_prefix_guild_id = str(ctx.guild.id)

        set_prefix_check = f"SELECT * FROM slash_command_setup WHERE guild_id = %s"
        set_prefix_check_values = [set_prefix_guild_id]

        my_cursor.execute(set_prefix_check, set_prefix_check_values)
        all_prefix = my_cursor.fetchone()
        
        standard_prefix = "?"
        
        
        if all_prefix:
            
            if prefixe == all_prefix[1]:
    
                emb = discord.Embed(title="Gleicher Prefix", description="Der Prefix wird bereits von Ihnen verwendent", color=discord.Colour.random())
                await ctx.respond(embed=emb)

            else:
                
                try:

                    set_prefix = f"UPDATE slash_command_setup SET prefix = %s WHERE guild_id = %s"
                    set_prefix_values = (prefixe, set_prefix_guild_id)
                    my_cursor.execute(set_prefix, set_prefix_values)
                    setup_db.commit()

                    emb = discord.Embed(title="Prefix Erfolgreich geändert", 
                        description=f"Der Prefix wurde Erfolgreich geändert. Aktuelle Prefix: **{prefixe}**", color=discord.Colour.brand_green())
                    await ctx.respond(embed=emb)

                except mysql.connector.Error as error:
                    print("parameterized query failed {}".format(error))

                finally:

                    if setup_db.is_connected():
                            
                        my_cursor.close()
                        setup_db.close()

                    else:
                        pass
            
        else:
                
            try:

                insert_setup_guild = """ INSERT INTO slash_command_setup (guild_id, prefix) VALUES (%s, %s)"""
                setup_guild_values = [set_prefix_guild_id, standard_prefix]
                my_cursor.execute(insert_setup_guild, setup_guild_values)
                setup_db.commit()

                emb = discord.Embed(title="Fehler", 
                description=f"""
                Dieser Server wurde noch nicht Regestriert.
                Der Server wurde jetzt nachträglich Registirert versuchen sie es doch gleich nochmal den Prefix zu ändern.
                """, color=error_red)
                await ctx.respond(embed=emb)

            except mysql.connector.Error as error:
                print("parameterized query failed {}".format(error))

            finally:

                    if setup_db.is_connected():
                    
                        my_cursor.close()
                        setup_db.close()

                    else:
                        pass

    

    @commands.slash_command()
    async def show_prefix(self, ctx):

        setup_db = self.set_prefix_connect()
        my_cursor = setup_db.cursor()

        set_prefix_guild_id = str(ctx.guild.id)

        set_prefix_check = (f"SELECT * FROM slash_command_setup WHERE guild_id = %s")
        set_prefix_check_values = [set_prefix_guild_id]

        my_cursor.execute(set_prefix_check, set_prefix_check_values)
    	
        all_prefix = my_cursor.fetchone()
        all_prefix_formatted = all_prefix[1]
        
        emb = discord.Embed(title="Dein Prefix", 
            description=f"Der Prefix für diesen Server ist **{all_prefix_formatted}** wenn sie einen anderen haben möchten benutzen sie den set-prefix command", color=discord.Colour.random())
        await ctx.respond(embed=emb)



def get_prefix(bot, message):

    setup_connector = mysql.connector.connect(host='localhost', user='root', password=os.getenv("sql_passwort"), database='setup')

    setup_db = setup_connector
    my_cursor = setup_db.cursor()

    set_prefix_guild_id = message.guild.id
    set_prefix_guild_id_str = str(set_prefix_guild_id)
    
    guild_check = (f"SELECT * FROM slash_command_setup WHERE guild_id = %s")
    guild_check_values = [set_prefix_guild_id_str]

    my_cursor.execute(guild_check, guild_check_values)
        
    all_guilds = my_cursor.fetchone()

    prefixes_first = all_guilds[1]

    return prefixes_first

#Intents
intent = discord.Intents.default()
intent.members = True
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=(get_prefix), intents=intents)


bot.remove_command("help")

error_red = discord.Colour.brand_red()
funpark_colour = 0xb136bf

no_author_emb = discord.Embed(title="Du bist nicht berechtigt", description=f"Du bist nicht berechtigt diesen Knopf zu drücken nur admins durfen mit diesen Command interagieren",color = error_red)


bot.add_cog(setup_control(bot))


class Help_menu(discord.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def help (self, ctx):

        embed = discord.Embed(
        title= f"This is the Help menu from {bot.user.name}",
        description= f"The help menu is divided into several sections **the Prifix is {get_prefix}**",
        color= discord.Colour.orange())
        embed.add_field(name="Funcommands", value=f"`lick` `idk` `fbi` `kiss` `hug` `puch` `marry`\n `dance` `gif` `aboutme ` `RPS` `coinflip` `surprise` `wink` `pat` `feed` `cuddle` `animememe`", inline=False)
        
        embed.add_field(name="Moderationtolls", value=f"`dm` `ban` `kick` `clear` `say`", inline=False)
        embed.add_field(name="Summer event", value=f"`cocktails`", inline=False)
        await ctx.send (embed=embed)


     
bot.add_cog(Help_menu(bot))




