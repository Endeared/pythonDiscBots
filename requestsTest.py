import requests, json
from bs4 import BeautifulSoup

username = "name_here"
userList = f'https://api.roblox.com/users/get-by-username?username={username}'

headers = {
    "accept": "application/json"
}

response = requests.get(userList, headers=headers)
data = response.json()

userId = data['Id']
# print(json.dumps(data, indent=2))
print(userId)

usernameHistory = f'https://users.roblox.com/v1/users/{userId}/username-history?limit=100&sortOrder=Asc'
response = requests.get(usernameHistory, headers=headers)
data2 = response.json()

# print(json.dumps(data2, indent=2))
length = len(data2['data'])
print(length)
i = 0
names = []
while (i < length):
    names.append(data2['data'][i]['name'])
    i += 1
print(names)


































# placeId = 2996067865
# characterId = 43243255452432
# serverType = 0
# sortOrder = 2
# excludeFullGames = False
# limit = 10
# # gameServerList = f'http://census.daybreakgames.com/get/ps2:v2/character/?character_id=5428018587875812257&c:show=name'
# gameServerList = f'http://census.daybreakgames.com/get/ps2:v2/character/?name.first_lower=cephro'

# headers = {
#     "accept": "application/json"
# }

# response = requests.get(gameServerList, headers=headers)
# data = response.json()

# charId = data['character_list'][0]['character_id']
# factionId = data['character_list'][0]['faction_id']
# hours = int((data['character_list'][0]['times']['minutes_played'])) / 60
# charName = data['character_list'][0]['name']['first']
# battleRank = data['character_list'][0]['battle_rank']['value']
# battleRankPerc = data['character_list'][0]['battle_rank']['percent_to_next']


# rounded = round(hours)
# count = int(factionId)


# if count == 3:
#     factionId = 'Terran Republic'
#     print(factionId)
# elif count == 2:
#     factionId = 'New Conglomerate'
#     print(factionId)
# elif count == 1:
#     factionId = 'Vanu Sovereignty'
#     print(factionId)

# print(charId)
# print(charName)
# print(rounded)
# print(battleRank)
# print(battleRankPerc)


# gameServerList2 = f'http://census.daybreakgames.com/get/ps2:v2/characters_online_status/?character_id={charId}'


# response2 = requests.get(gameServerList2, headers=headers)
# data2 = response2.json()

# onlineStatus = data2['characters_online_status_list'][0]['online_status']

# statusCheck = int(onlineStatus)

# if statusCheck == 0:
#     onlineStatus = 'Offline'
#     print(onlineStatus)
# elif statusCheck == 1:
#     onlineStatus = 'Online'
#     print(onlineStatus)

#converts json object and returns as indented string to make look nice
# print(json.dumps(data, indent=2))






# import requests, json
# from bs4 import BeautifulSoup

# placeId = 2996067865
# serverType = 0
# sortOrder = 2
# excludeFullGames = False
# limit = 10
# gameServerList = f"https://games.roblox.com/v1/games/{placeId}/servers/{serverType}?sortOrder={sortOrder}&excludeFullGames={excludeFullGames}&limit={limit}"

# headers = {
#     "accept": "application/json"
# }

# response = requests.get(gameServerList, headers=headers)
# data = response.json()

# #converts json object and returns as indented string to make look nice
# print(json.dumps(data, indent=2))







# import requests, json
# from bs4 import BeautifulSoup

# gameIdArr = [
#     2996067865,
#     10141792191,
#     5847686787,
# ]


# serverType = 0
# sortOrder = 2
# excludeFullGames = False
# limit = 10
# placeId = 2996067865

# length = len(gameIdArr)


# # for i in range(3):

#     # placeId = gameIdArr[i]
# gameServerList = f"https://games.roblox.com/v1/games/{placeId}/servers/{serverType}?sortOrder={sortOrder}&excludeFullGames={excludeFullGames}&limit={limit}"

# headers = {
#     "accept": "application/json"
# }

# response = requests.get(gameServerList, headers=headers)
# data = json.dumps(response.json())
# check = json.loads(data)
# print(json.dumps(data, indent=2))

    # try:
    #     serverInfo = check['data'][0]
    # except IndexError:
    #     pass

    # playing = serverInfo["playing"]

    # if playing > 10:
    #     print(check)
    #     print(serverInfo["playing"])
    #     print(gameIdArr[i])
    #     print(True)

    # if playing < 10:
    #     print(False)





# converts json object and returns as indented string to make look nice
# print(json.dumps(data, indent=2))
# for serverCheck in check["playing"]:
#     if "playing" in serverCheck:
#         print(serverCheck["playing"])
