
from Hanime_Funpark import *
from discord import ButtonStyle, Colour, Embed, Interaction, CategoryChannel
from Import_file import *
from Liest import *
from level_sytem import * 
from dotenv import load_dotenv
import calendar


@bot.slash_command(description="Shows you the ping.")
async def ping(ctx):
    await ctx.respond(f"Pong! Latency is ``{round(bot.latency*1000)}`` ms")


   
class Update(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def update(self, ctx):
        emb = discord.Embed(
            title="Update",
            description=f"Hello all together I {bot.user.name} was updated again:",
            color= discord.Colour.purple()
        )
        
        emb.add_field(name="New functions ", value="We have added new fun commands (?help) and the RPS game is now much better and more fun commands ")
        await ctx.send(embed=emb)

bot.add_cog(Update(bot))



class main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
         
        view = View(timeout=None)
        print(f'Logged in as: {bot.user.name}')
        print(f'With ID: {bot.user.id}')
        self.bot.loop.create_task(status_task())
         
        print("┏━━━┓ ┏━━━┓ ┏┓ ┏┓ ┏━━┓ ┏━━━┓ ┏━━┓")
        print("┃┏━┓┃ ┃┏━┓┃ ┃┃ ┃┃ ┗┫┣┛ ┗┓┏┓┃ ┗┫┣┛")
        print("┃┗━━┓ ┃┃ ┃┃ ┃┃ ┃┃  ┃┃   ┃┃┃┃  ┃┃")
        print("┗━━┓┃ ┃┗━┛┃ ┃┃ ┃┃  ┃┃   ┃┃┃┃  ┃┃")
        print("┃┗━┛┃ ┗━━┓┃ ┃┗━┛┃ ┏┫┣┓ ┏┛┗┛┃ ┏┫┣┓")
        print("┗━━━┛    ┗┛ ┗━━━┛ ┗━━┛ ┗━━━┛ ┗━━┛")

        # level system
        self.bot.add_view(levelup_channel_buttons())
        self.bot.add_view(level_roles_buttons_level())
        self.bot.add_view(level_roles_buttons_role())
        self.bot.add_view(reset_level_button())
        
        # self roles 
        self.bot.add_view(DropdownColours())
        self.bot.add_view(DropdownHoppys())
        view.add_item(Genderbutton_Female())
        view.add_item(Genderbutton_Divers())
        view.add_item(Genderbutton_Male())

        self.bot.add_view(view)

bot.add_cog(main(bot))



@bot.command(aliases=['user-info', 'about', 'whois', 'ui'])
async def userinfo(ctx, member: discord.Member = None):
    member = ctx.author if not member else member

    unix_join_time = calendar.timegm(member.joined_at.utctimetuple())
    unix_create_time = calendar.timegm(member.created_at.utctimetuple())

    badge = ""
    if member.public_flags.bug_hunter:
        badge += "<:bughunter:1045796473691979776> Bug Hunter\n"
    if member.public_flags.bug_hunter_level_2:
        badge += "<:bughunter2:1045796474744750090> Bug Hunter Level 2\n"
    if member.public_flags.early_supporter:
        badge += "<:earlysupporter:1045796475864625283> Early Suppoter\n"
    if member.public_flags.verified_bot_developer:
        badge += "<:botdev:1045796472408506368> Developer\n"
    if member.public_flags.partner:
        badge += "<:partner:1045796481518551102> Partner\n"
    if member.public_flags.staff:
        badge += "<:staff:1045796482705543168> Staff\n"
    if member.public_flags.hypesquad_balance:
        badge += f"<:hypesquad_balance:1045796476992884838> Hypesquad Balance\n"
    if member.public_flags.hypesquad_bravery:
        badge += f"<:hypesquad_bravery:1045796478507032638> Hypesquad Bravery\n"
    if member.public_flags.hypesquad_brilliance:
        badge += f"<:hypesquad_brilliance:1045796480172163152> Hypesquad Brilliance\n"

    user_banner = await bot.fetch_user(member.id)

    if user_banner.banner is not None:
        if member.avatar is not None:
            embed = discord.Embed(colour=member.color,
                                timestamp=datetime.utcnow(),
                                description=f"[User Avatar]({member.avatar.url}) | [User Banner]({user_banner.banner.url})")
            embed.set_image(url=f"{user_banner.banner.url}")
            embed.set_thumbnail(url=f'{member.display_avatar.url}')
        else:
            embed = discord.Embed(colour=member.color,
                                timestamp=datetime.utcnow(),
                                description=f"[User Banner]({user_banner.banner.url})")
            embed.set_image(url=f"{user_banner.banner.url}")
    elif member.avatar is not None:
        embed = discord.Embed(colour=member.color,
                                timestamp=datetime.utcnow(),
                                description=f"[User Avatar]({member.avatar.url})")
        embed.set_thumbnail(url=f'{member.display_avatar.url}')
    else:
        embed = discord.Embed(colour=member.color,
                                timestamp=datetime.utcnow())

    embed.set_author(name=f"Userinfo")

    embed.add_field(name="Name:",
                    value=f"`{member} (Bot)`" if member.bot else f"`{member}`",
                    inline=True)
    embed.add_field(name=f"Mention:",
                    value=member.mention,
                    inline=True)
    embed.add_field(name="Nick:",
                    value=f"`{member.nick}`" if member.nick else "Nicht gesetzt",
                    inline=True)
    embed.add_field(name="ID:",
                    value=f"`{member.id}`",
                    inline=True)

    if member.status == discord.Status.online:
        if member.is_on_mobile():
            embed.add_field(name="Status:", value="`Handy`")
        else:
            embed.add_field(name="Status", value=f"`Online`")
    elif member.status == discord.Status.idle:
        embed.add_field(name="Status:",
                        value=f"`Abwesend`")
    elif member.status == discord.Status.dnd:
        embed.add_field(name="Status:",
                        value=f"`Beschäftigt`")
    elif member.status == discord.Status.offline:
        embed.add_field(name="Status:",
                        value=f"`Offline`")
    elif member.status == discord.Status.invisible:
        embed.add_field(name="Status:",
                        value=f"`Unsichtbar`")

    embed.add_field(name="Erstellt am:",
                    value=f"<t:{unix_create_time}:f> (<t:{unix_create_time}:R>)",
                    inline=True)
    embed.add_field(name="Beigetreten am:",
                    value=f'<t:{unix_join_time}:f> (<t:{unix_join_time}:R>)',
                    inline=True)
    embed.add_field(name="Höchste Rolle:",
                    value=member.top_role.mention,
                    inline=True)
    embed.add_field(name="<:booster:1045801339780862063> Booster:",
                    value=f"`Ja`" if member.premium_since else "`Nein`",
                    inline=True)
    if badge != "":
        embed.add_field(name="Badges:",
                        value=badge,
                        inline=True)

    if member.activities:
        for activity in member.activities:
            if str(activity) == "Spotify":
                embed.add_field(name="Spotify",
                                value=f'Title: {activity.title}\nArtist: {activity.artist}\n')

    embed.set_thumbnail(url=f'{member.avatar.url}')

    await ctx.reply(embed=embed)


if __name__ == "__main__":
    for filename in os.listdir("cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")

    load_dotenv()
    bot.run(os.getenv("TOKEN"))

