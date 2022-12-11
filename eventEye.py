import os
import discord
from dotenv import load_dotenv
import ctypes


ctypes.windll.kernel32.SetConsoleTitleW("EventEye")

BOT_NAME = "EventEye"
load_dotenv()
DISCORD_TOKEN = os.getenv("EVENTEYE")

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)
botId = 1049508281351143456
clientId = 788512346267320331

channelId = 1049488120942440501

links = [
    "https://www.roblox.com/games/424511221/priv-servers-RCL"
]

myUrl = "https://www.roblox.com/users/13202550/profile"


@bot.event
async def on_ready():
    print(f'{bot.user} is online.')


@bot.event
async def on_message(message):

    if (message.channel.id != 1049488120942440501):
        return

    if message.author.id == botId:
        return

    if message.author.id != clientId:
        return

    checkChannel = bot.get_channel(1049488120942440501)
    check = await checkChannel.fetch_message(checkChannel.last_message_id)

    typeChannel = bot.get_channel(1049509182388305993)
    officialChannel = bot.get_channel(1049767952985108621)
    s2nChannel = bot.get_channel(1049768751538647040)

    if check.author.id != clientId:
        return

    print(check)

    words = []
    words = check.content.split(" ][ ")

    place = words[0]
    serverName = words[1]
    refLink = words[2]
    placeValue = words[3]

    embed = discord.Embed(title="Event detected!",
                          url=place,
                          description=(f'An event has been found. Click the blue link above to go there!\nNote: You may have to join said Discord to participate.'),
                          color=0x5B03FF)
    embed.set_author(name="EventEye",
                     icon_url="https://i.imgur.com/CXHsRBF.png")
    embed.add_field(name="Server",
                    value=f'[{serverName}]({refLink})',
                    inline=True)
    embed.add_field(name="Location",
                    value=placeValue,
                    inline=True)
    embed.set_footer(text=f'EventEye 1.0 - made by haypro#0004')

    await typeChannel.send(embed=embed)
    # await officialChannel.send(embed=embed)
    # await s2nChannel.send(embed=embed)
    # await typeChannel.send(f'Practice request sent in {channelName} in {serverName}, requested by {user}#{userId}. Practice link: {place}')

    return


bot.run('TOKEN_HERE')
