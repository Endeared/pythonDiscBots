import discord
import logging
import asyncio
import os
import json
import ctypes


ctypes.windll.kernel32.SetConsoleTitleW("EventBot")

client = discord.Client()

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

channelIds = [
            751457496345870346,
            137274833909055488,
            1049501754716336208,
            631033295961980928,
            309410914619097091,
            ]

refLinks = [
            "https://www.roblox.com/groups/5665804/Snow-Core#!/about",
            "https://www.roblox.com/groups/3747606/The-WIJ-Alliance#!/about",
            "https://www.roblox.com/users/13202550/profile",
            "https://www.roblox.com/groups/2742631/The-Galactic-Republic#!/about",
            "https://www.roblox.com/groups/14638/RSF#!/about",
]

placeValues = [
            "Aurora's Dam",
            "Crystal Cove",
            "Port Maersk",
            "Glacian Factory",
            "Indigo II",
            "FutureTops",
            "outflash's RCL",
            "Ordana",
            "Docks",
            "FTops Rework",
            "SC Pitgrounds",
]

validPlaces = [
            "5361853069",
            "4727031612",
            "2007375127",
            "5841467683",
            "1427569028",
            "5188367351",
            "424511221",
            "6564224471",
            "4632428105",
            "5169051062",
            "6941660837",
            ]

length = len(channelIds)

clientId = 296106771087491073

print("test")


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):

    channel = message.channel.id

    if channel not in channelIds:
        return

    if channel in channelIds:

        checkChannel = client.get_channel(channel)
        check = await checkChannel.fetch_message(checkChannel.last_message_id)
        # print(checkChannel)
        # print(check)

        for x in validPlaces:

            if x in check.content:

                xIndex = validPlaces.index(x)
                refIndex = channelIds.index(channel)

                words = []
                words = check.content.split(" ")

                for word in words:

                    print(word)
                    if 'https://www.roblox.com/games' in word:


                        typeChannel = client.get_channel(1049488120942440501)
                        index = words.index(word)
                        place = words[index]

                        result = place[place.find("https:"):]
                        print(result)

                        channelName = checkChannel.name
                        refLink = refLinks[refIndex]
                        placeValue = placeValues[xIndex]
                        serverName = check.guild.name
                        user = check.author.name
                        userId = check.author.discriminator
                        discordId = check.author.id

                        print(f'{discordId} ][ {result}')

                        data = {}
                        data['server'] = f'{place}'
                        data['clan'] = f'{serverName}'
                        data['reference'] = f'{refLink}'
                        data['user'] = f'{user}'
                        data['userId'] = f'{userId}'
                        data['channel'] = f'{channelName}'
                        data['placeValue'] = f'{placeValue}'
                        data['discordId'] = f'{discordId}'

                        json_data = json.dumps(data, indent=2)
                        print(json_data)
                        with open(r'''C:\Users\hamey.DESKTOP-MULCHGK\Desktop\jquery-test\data.json''', 'w') as f:
                            f.write(json_data)

                        await typeChannel.send(f'{result} ][ {serverName} ][ {refLink} ][ {placeValue}')


print("test")
client.run('TOKEN_HERE')
