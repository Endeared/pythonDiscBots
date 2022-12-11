from asyncio import tasks
import os
import discord
from dotenv import load_dotenv
import requests
import json
from bs4 import BeautifulSoup
import asyncio
import time
import ctypes


ctypes.windll.kernel32.SetConsoleTitleW("RaidEye")


BOT_NAME = "RaidEye"
load_dotenv()
DISCORD_TOKEN = os.getenv("RAIDEYE")

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)


urlArray = [
    "https://www.roblox.com/games/5841467683/Glacian-Factory-RAID",
    "https://www.roblox.com/games/5361853069/Auroras-Dam-RAID",
    "https://www.roblox.com/games/6101349068/Blizzard-Outfall-RAID",
    "https://www.roblox.com/games/5014397267/RAID-Reversal-Compound",
    "https://www.roblox.com/games/6565314611/RAID-Unity-Outfall",
    "https://www.roblox.com/games/8771989818/RAID-Reversal-Compound-Remastered",
    "https://www.roblox.com/games/10141792191/RAID-The-Graveyard",
    "https://www.roblox.com/games/5847686787/SWORD-Tafes-Pass",
    "https://www.roblox.com/games/7257291581/RAID-The-Collective",
    "https://www.roblox.com/games/1427493600/WIJ-Outpost-Indigo-II",
    "https://www.roblox.com/games/1427580544/WIJ-Outpost-Cerulean-II",
    "https://www.roblox.com/games/5257899796/WIJ-Marrs-Communications-Relay-FAIRZONE",
    "https://www.roblox.com/games/4652767371/Raidable-Docks-Fairzone",
    "https://www.roblox.com/games/2007110262/Port-Maersk-EASY-MODE",
    "https://www.roblox.com/games/7775216059/RAID-Armageddon-Shipyard",
    "https://www.roblox.com/games/8249245310/RAID-Vulturist-Tower",
    "https://www.roblox.com/games/11401909704/RAID-Pride-of-Altaris",
    "https://www.roblox.com/games/11412621623/RAID-Starfall-Station",
    "https://www.roblox.com/games/9166246939/RAID-Malora-District",
    "https://www.roblox.com/games/11117968023/6v6-NEW-Crown-of-Polaris",
    "https://www.roblox.com/games/8152027924/RSF-Winter-Arvore-II#!/about",
    "https://www.roblox.com/games/9726482460/Installation-Anchorage",
    "https://www.roblox.com/games/8046351934/RAID-Dawn-Under-Heaven",
    "https://www.roblox.com/games/8254413158/Blacksite-Ares"
]

imgArr = [
    "https://tr.rbxcdn.com/d7c01ebfc7d898dff08ffedc4b68250f/768/432/Image/Png",
    "https://tr.rbxcdn.com/03a2f2f0dba2241cf291965879914676/768/432/Image/Png",
    "https://tr.rbxcdn.com/e6d91b528f99087113ff582b9e5349ad/768/432/Image/Png",
    "https://tr.rbxcdn.com/e9c71a7684c8e65257a04d4fd4b8c449/768/432/Image/Png",
    "https://tr.rbxcdn.com/2396c7bb94d7c63f38ded1328f82eaa5/768/432/Image/Png",
    "https://tr.rbxcdn.com/965465bfea5161e703010834a53e3577/768/432/Image/Png",
    "https://t7.rbxcdn.com/5c66ba63087a3dd4cfa7b5c4717f6065",
    "https://tr.rbxcdn.com/bab82f223d8d05f7068cc0e2b168a411/768/432/Image/Png",
    "https://tr.rbxcdn.com/1f89fc2b5c0234f5c3871a2405aa8a26/768/432/Image/Png",
    "https://tr.rbxcdn.com/f27bca028fdbdaaae5e14561599d2bfb/768/432/Image/Png",
    "https://tr.rbxcdn.com/808605d3b34c74bf02c7115585340e35/768/432/Image/Png",
    "https://tr.rbxcdn.com/9844e6883685d0e9ac8f69739f89cecc/768/432/Image/Png",
    "https://tr.rbxcdn.com/997960976f37f8d23a631c591620cd4a/768/432/Image/Png",
    "https://tr.rbxcdn.com/c03068cc7a411ab374df6bd0bc69671e/768/432/Image/Png",
    "https://tr.rbxcdn.com/41efc88d9796fa4b480e985c2245a836/768/432/Image/Png",
    "https://tr.rbxcdn.com/9966c1b993205996f1453a9e66a7a5f3/768/432/Image/Png",
    "https://tr.rbxcdn.com/b17e86f05e9c9e8123c8f1e5f779e4ee/768/432/Image/Png",
    "https://tr.rbxcdn.com/e68faf5a3a2080f27467306f4486ff0f/768/432/Image/Png",
    "https://t2.rbxcdn.com/45b31d4505d514928adfca9a7271d55e",
    "https://t7.rbxcdn.com/5c66ba63087a3dd4cfa7b5c4717f6065",
    "https://t1.rbxcdn.com/162138bbcfc4f93e3f26c790c6813acc",
    "https://tr.rbxcdn.com/5d3294f63bf1f9ac268799cc4d1f56da/768/432/Image/Png",
    "https://tr.rbxcdn.com/b83523c44c362851ca976aeb47711b04/768/432/Image/Png",
    "https://tr.rbxcdn.com/71ee13ad60ecb7cecda73e695ec58a7a/768/432/Image/Png",
]

gameIdArr = [
    5841467683,
    5361853069,
    6101349068,
    5014397267,
    6565314611,
    8771989818,
    10141792191,
    5847686787,
    7257291581,
    1427493600,
    1427580544,
    5257899796,
    4652767371,
    2007110262,
    7775216059,
    8249245310,
    11401909704,
    11412621623,
    9166246939,
    11117968023,
    8152027924,
    9726482460,
    8046351934,
    8254413158
]

locArr = [
    "Glacian Factory",
    "Aurora's Dam",
    "Blizzard Outfall",
    "Reversal Compound",
    "Unity Outfall",
    "Reversal Compound 2",
    "Graveyard",
    "Tafes Pass",
    "Collective",
    "Indigo 2",
    "Cerulean 2",
    "Marrs Relay",
    "Docks",
    "Port Maersk",
    "Armageddon Shipyard",
    "Vulturist Tower",
    "Pride of Altaris",
    "Starfall Station",
    "Malora District",
    "Crown of Polaris",
    "Arvore 2",
    "Installation Anchorage",
    "Dawn Under Heaven",
    "Blacksite Ares"
]

skip = []

hour = []

hourCheck = 0
length = len(urlArray)

serverType = 0
sortOrder = 2
excludeFullGames = False
limit = 10


@bot.event
async def on_ready():
    print(f'{bot.user} is online.')

    while (True):
        for hourCheck in range(36):

            try:
                if hour[0] == 0:
                    if hourCheck == 35:
                        skip.clear()
                        hour.clear()
            except IndexError:
                pass

            try:
                if hour[0] != 0:
                    if hourCheck == hour[0] - 1:
                        skip.clear()
                        hour.clear()
            except IndexError:
                pass

            print(hourCheck)
            for i in range(length):
                if i not in skip:

                    await asyncio.sleep(5)

                    URL = urlArray[i]
                    page = requests.get(URL)
                    soup = BeautifulSoup(page.content, "html.parser")

                    try:
                        clanName = soup.find(
                            'a', {'class': 'text-name text-overflow'}).get_text()
                    except AttributeError:
                        pass

                    thumbnail = imgArr[i]
                    print(URL)
                    # print(hourCheck)
                    # print(skip)
                    # print(hour)
                    # print(clanName)
                    # print(locArr[i])

                    placeId = gameIdArr[i]
                    gameServerList = f"https://games.roblox.com/v1/games/{placeId}/servers/{serverType}?sortOrder={sortOrder}&excludeFullGames={excludeFullGames}&limit={limit}"

                    headers = {
                        "accept": "application/json"
                    }

                    response = requests.get(gameServerList, headers=headers)
                    data = json.dumps(response.json())
                    check = json.loads(data)
                    playingCount = 0

                    try:
                        serverInfo = check['data'][0]
                    except IndexError:
                        await asyncio.sleep(5)
                        playingCount = 0
                        pass
                    except KeyError:
                        await asyncio.sleep(5)
                        playingCount = 0
                        pass

                    try:
                        playingCount = serverInfo["playing"]
                    except KeyError:
                        await asyncio.sleep(5)
                        playingCount = 0
                        pass
                    except IndexError:
                        await asyncio.sleep(5)
                        playingCount = 0
                        pass
                    except UnboundLocalError:
                        await asyncio.sleep(5)
                        playingCount = 0
                        pass

                    print(playingCount)
                    # print(gameIdArr[i])

                    embed = discord.Embed(title="Raid detected!",
                                          url=URL,
                                          description=f"There is currently {playingCount} or more players at this base. Click the blue link above to go there.",
                                          color=0xEFF33F)

                    embed.set_thumbnail(url=thumbnail)

                    embed.set_author(name="RaidEye",
                                     icon_url="https://i.imgur.com/tmfv3VU.png")

                    embed.add_field(name="Clan",
                                    value=clanName,
                                    inline=True)

                    embed.add_field(name="Location",
                                    value=locArr[i],
                                    inline=True)

                    embed.set_footer(text="RaidEye 1.0 - by haypro#0004")

                    if playingCount >= 10:
                        botChannel = bot.get_channel(1047910209881903196)
                        s2nRaidChannel = bot.get_channel(1048256564705886259)
                        officialChannel = bot.get_channel(1049037231433732226)
                        await botChannel.send(embed=embed)
                        # await s2nRaidChannel.send(embed=embed)
                        # await officialChannel.send(embed=embed)
                        print(True)
                        skip.append(i)
                        hour.append(hourCheck)
                        playingCount = 0

                    if playingCount < 10:
                        print(False)
                        playingCount = 0



bot.run('TOKEN_HERE')
