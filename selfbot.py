import discord
import logging
import asyncio
import ctypes


ctypes.windll.kernel32.SetConsoleTitleW("PracSelfbot")


client = discord.Client()


channelIds = [
            848240885903917086,
            759525108879720448,
            835208120346476544,
            777693445292032042,
            1048069636232593468
            ]

verifiedPlayers = [
                    450850796255313932,
                    128660683083612160,
                    331495097025822721,
                    544667411165741066,
                    211250677937209344,
                    889634157167271936,
                    576121988343660554,
                    365663162592395266
                    ]

verifiedPlayersNames = [
                    'haypro',
                    'Moist_God',
                    'doorvpn',
                    'shockage',
                    'EliteMorality',
                    'Latedownload',
                    'EnigmaPenguin',
                    'ReaperMagic'
]

length = len(channelIds)

aimTheoryId = 848240885903917086
futuretopsId = 759525108879720448
rcnId = 835208120346476544
gccId = 777693445292032042
testId = 1048069636232593468

clientId = 819477267355926568

ignoreId = []
ignorePlace = []

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    while (True):
        await asyncio.sleep(1800)
        ignoreId.clear()
        ignorePlace.clear()

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

        if 'https://www.roblox' in check.content:

            # print(check.content)
            words = []
            words = check.content.split(" ")
            # print(words)

            for word in words:

                print(word)
                if 'https://www.roblox.com/games' in word:

                    typeChannel = client.get_channel(1047982135635628055)
                    index = words.index(word)
                    place = words[index]
                    channelName = checkChannel.name
                    serverName = check.guild.name
                    user = check.author.name
                    userId = check.author.discriminator
                    discordId = check.author.id

                    print(f'{discordId} ][ {place}')
                    print(ignoreId)
                    print(ignorePlace)

                    if discordId in ignoreId:
                        return

                    if place in ignorePlace:
                        return

                    if discordId in verifiedPlayers:
                        userIndex = verifiedPlayers.index(discordId)
                        user = verifiedPlayersNames[userIndex]
                        await typeChannel.send(f'{channelName}][{serverName}][{user}][{userId}][{place}][UNIQUE')
                        ignoreId.append(discordId)
                        ignorePlace.append(place)
                        return

                    await typeChannel.send(f'{channelName}][{serverName}][{user}][{userId}][{place}')


client.run('TOKEN_HERE')
