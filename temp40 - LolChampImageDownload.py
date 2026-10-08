import json
import requests

with open("./data/lol_champion.json", "r", encoding="utf-8") as f:
    data = json.load(f)

y = [i for i in data["data"]]

j = 0
for i in y:
    data = requests.get(f"https://ddragon.leagueoflegends.com/cdn/16.17.1/img/champion/{i}")
    data.raise_for_status()
    with open(f"./data/img/lol/champion/{j}.png", "wb") as f:
        f.write(data.content)
    j += 1