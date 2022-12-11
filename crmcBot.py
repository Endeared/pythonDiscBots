import discord
from discord.ext import commands
from discord.utils import get
import os
import requests, json
from bs4 import BeautifulSoup

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
bot_channel = 1050111880632479844

rank_dict = {
  "Commandant" : "COMM",
  "Senior Officer" : "SO",
  "Junior Officer" : "JO",
  "Task Force" : "TF",
  "Operator" : "OPT",
  "Specialist" : "SPC",
  "Cadet" : "CDT",
  "Initiate" : "INT",
}

def get_char_info(playerName):
    lowerCaseName = playerName.lower()
    gameServerList = f'http://census.daybreakgames.com/get/ps2:v2/character/?name.first_lower={lowerCaseName}'
    headers = {
        "accept": "application/json"
    }
    response = requests.get(gameServerList, headers=headers)
    data = response.json()
    charId = data['character_list'][0]['character_id']
    factionId = data['character_list'][0]['faction_id']
    hours = int((data['character_list'][0]['times']['minutes_played'])) / 60
    charName = data['character_list'][0]['name']['first']
    battleRank = data['character_list'][0]['battle_rank']['value']
    battleRankPerc = data['character_list'][0]['battle_rank']['percent_to_next']
    username = data["character_list"][0]["name"]["first"]

    rounded = round(hours)
    count = int(factionId)

    if count == 3:
        factionId = 'Terran Republic'
        print(factionId)
    elif count == 2:
        factionId = 'New Conglomerate'
        print(factionId)
    elif count == 1:
        factionId = 'Vanu Sovereignty'
        print(factionId)

    list = []
    list.append(charId) # 0
    list.append(charName) # 1
    list.append(rounded) # 2
    list.append(battleRank) # 3
    list.append(battleRankPerc) # 4
    list.append(username) # 5

    gameServerList2 = f'http://census.daybreakgames.com/get/ps2:v2/characters_online_status/?character_id={charId}'
    response2 = requests.get(gameServerList2, headers=headers)
    data2 = response2.json()
    onlineStatus = data2['characters_online_status_list'][0]['online_status']
    statusCheck = int(onlineStatus)

    if statusCheck == 0:
        onlineStatus = 'Offline'
        list.append(onlineStatus)
    elif statusCheck == 1:
        onlineStatus = 'Online'
        list.append(onlineStatus)

    return list

def get_outfit_info(playerName):
    lowerCaseName = playerName.lower()
    gameServerList2 = f'http://census.daybreakgames.com/get/ps2:v2/character/?name.first_lower={lowerCaseName}'
    headers = {
        "accept": "application/json"
    }
    response2 = requests.get(gameServerList2, headers=headers)
    data2 = response2.json()
    charId = data2['character_list'][0]['character_id']

    gameServerList = f'http://census.daybreakgames.com/get/ps2:v2/outfit_member_extended/?character_id={charId}'

    response = requests.get(gameServerList, headers=headers)
    data = response.json()

    outfitRank = data['outfit_member_extended_list'][0]['member_rank']
    outfitName = data['outfit_member_extended_list'][0]['name']
    outfitTag = data['outfit_member_extended_list'][0]['alias']

    print(outfitRank)
    print(outfitName)
    print(outfitTag)
    list = []
    list.append(outfitRank) # 0
    list.append(outfitName) # 1
    list.append(outfitTag) # 2
    return list

def write_json(id, data):
    jsonPath = r'C:\Users\hamey.DESKTOP-MULCHGK\Desktop\GitHub\pythonBots\members.json'
    with open(jsonPath, 'r+', encoding="utf-8") as file:
        memberdata = {}
        memberdata[id] = data
        file.seek(0)
        json.dump(memberdata, file, indent = 2)
        file.close()

@bot.command(name='test')
async def test(ctx):
    sendChannel = bot.get_channel(bot_channel)
    await sendChannel.send(f'This is a test!')

@bot.command(name='rank')
async def showRank(ctx, playerName):
    sendChannel = bot.get_channel(bot_channel)
    rank = get_outfit_info(playerName)
    await sendChannel.send(rank[0])

@bot.command(name='outfit')
async def showRank(ctx, playerName):
    sendChannel = bot.get_channel(bot_channel)
    rank = get_outfit_info(playerName)
    await sendChannel.send(f'{rank[1]} [{rank[2]}]')

@bot.command(name='report')
async def report(ctx, playerName):
    sendChannel = bot.get_channel(bot_channel)
    charInfo = get_char_info(playerName)
    outfitInfo = get_outfit_info(playerName)

    embed = discord.Embed(title='PLAYER REPORT',
                            description=f'This is a player report for {charInfo[1]}.',
                            color=0xFF0000)
    embed.set_author(name="CRMC Bot")
    embed.add_field(name="Outfit Info",
                    value=f'{outfitInfo[1]} [{outfitInfo[2]}]\nRank: {outfitInfo[0]}',
                    inline=False)
    embed.add_field(name="Player Info",
                    value=f'Battle rank: {charInfo[3]} ({charInfo[4]}%)',
                    inline=False)
    embed.add_field(name="Hours Played",
                    value=f'{charInfo[2]}',
                    inline=False)

    await sendChannel.send(embed=embed)

@bot.command(name='register')
async def register(ctx, playerName):
    user = ctx.author
    userId = ctx.author.id

    jsonPath = r'C:\Users\hamey.DESKTOP-MULCHGK\Desktop\GitHub\pythonBots\members.json'
    with open(jsonPath, 'r') as file:
        members = json.load(file)
        if str(user.id) in members.keys() or any(d['name'] == playerName for d in members.values()):
            await ctx.send('already registered')
        else:
            importData = get_outfit_info(playerName)
            if importData[2] == 'CRMC':
                playerInfo = get_char_info(playerName)
                data = {
                        'discord_user': userId,
                        'character_id': playerInfo[0],
                        'name': playerInfo[5],
                        'outfit_rank': importData[0]
                }
                write_json(userId, data)
                await user.edit(nick='[{tag}] {user}'.format(tag=rank_dict[{importData[0]}], user=playerInfo[1]))
                role = discord.utils.get(ctx.guild.roles, name={importData[0]})
                await user.add_roles(role)
            else:
                await ctx.send('Please claim a character in Crimson Command.')
    file.close()


bot.run('TOKEN_HERE')
