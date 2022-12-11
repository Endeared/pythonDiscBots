import os
import discord
from dotenv import load_dotenv
import ctypes


ctypes.windll.kernel32.SetConsoleTitleW("PracEye")

BOT_NAME = "PracEye"
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN2")

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)
botId = 1047929263522848930
clientId = 819477267355926568

channelId = 1047200744245305407

links = [
    "https://www.roblox.com/games/424511221/priv-servers-RCL"
]


@bot.event
async def on_ready():
    print(f'{bot.user} is online.')


@bot.event
async def on_message(message):

    if (message.channel.id != 1047982135635628055):
        return

    if message.author.id == botId:
        return

    if message.author.id != clientId:
        return

    checkChannel = bot.get_channel(1047982135635628055)
    check = await checkChannel.fetch_message(checkChannel.last_message_id)

    typeChannel = bot.get_channel(1047953079837937744)
    officialChannel = bot.get_channel(1049012866176532531)
    s2nChannel = bot.get_channel(1048256526948778035)

    if check.author.id != clientId:
        return

    print(check)

    words = []
    words = check.content.split("][")

    channelName = words[0]
    serverName = words[1]
    user = words[2]
    userId = words[3]
    place = words[4]

    try:
        if words[5] == "UNIQUE":
            embed = discord.Embed(title="Spar request detected!",
                            url=place,
                            description="A spar request has been found. Click the blue link above to go there!",
                            color=0x90FF2C)
            embed.set_author(name="PracEye",
                            icon_url="https://i.imgur.com/748OVxw.png")
            embed.add_field(name="Player (VERIFIED)",
                            value=(f'{user} (:green_circle:)'),
                            inline=True)
            embed.add_field(name="Server",
                            value=serverName,
                            inline=True)
            embed.set_footer(text="PracEye 1.0 - made by haypro#0004")

            await typeChannel.send(embed=embed)
            await officialChannel.send(embed=embed)
            await s2nChannel.send(embed=embed)
            return
    except IndexError:
        pass


    embed = discord.Embed(title="Spar request detected!",
                          url=place,
                          description="A spar request has been found. Click the blue link above to go there!",
                          color=0x90FF2C)
    embed.set_author(name="PracEye",
                     icon_url="https://i.imgur.com/748OVxw.png")
    embed.add_field(name="Player",
                    value=(f'{user}#{userId}'),
                    inline=True)
    embed.add_field(name="Server",
                    value=serverName,
                    inline=True)
    embed.set_footer(text="PracEye 1.0 - made by haypro#0004")

    print("Practice request sent in " + checkChannel.name + " in " + check.guild.name + ", requested by " +
          check.author.name + "#" + check.author.discriminator + ". Practice link: " + place)

    await typeChannel.send(embed=embed)
    await officialChannel.send(embed=embed)
    await s2nChannel.send(embed=embed)
    # await typeChannel.send(f'Practice request sent in {channelName} in {serverName}, requested by {user}#{userId}. Practice link: {place}')

    return


bot.run('TOKEN_HERE')
