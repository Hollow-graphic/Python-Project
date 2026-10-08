import json

with open("data\\lol\\match\\14-52_01-09-2026.json", "r", encoding="utf-8") as f:
    data = json.load(f)

ap_champ_name = data["activePlayer"]["abilities"]["E"]["id"][:-1]
ap_champ_level = data["activePlayer"]["level"]
ap_champ_gold = data["activePlayer"]["currentGold"]

print("ap_champ_name: ", ap_champ_name)
print("ap_champ_level: ", ap_champ_level)
print()
print("ap_champ_gold: ", ap_champ_gold)

all_player = data["allPlayers"]

for i in all_player:
    print("----")
    print("RiotId: ", i["riotId"])
    print("Champ: ", i["championName"])
    print("Level: ", i["level"])
    print("Score: ", i["scores"])
    items = [[],[],[],[],[],[]]
    for j in i["items"]:
        items[j["slot"]-1] = [j["itemID"], j["displayName"]]
    print("items: ", items)
    print("Summoner: ", [i["summonerSpells"][j]["displayName"] for j in i["summonerSpells"]])
    