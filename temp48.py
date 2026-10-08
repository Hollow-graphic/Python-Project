import json
from pathlib import Path
import random

file = random.choice([file for file in Path("./data/lol/match").glob("*.json")])

user_puuid = "JQa5YtgqtTkm97DiS9RNnrAWojYq6xcUMHShveWZ4MOutYl9shSnrTw-TACWpoq68z4v2cKEvr5rYA"

with open(file, "r", encoding="utf-8") as f:
    data = json.load(f)
    
info = data["info"]
player = info["participants"]
user = player[data["metadata"]["participants"].index(user_puuid)]

print("----")
print("GameId: ", str(file).split("\\match\\")[1][:-5])
print("GameMode: ", info["gameMode"], info["mapId"])
print("NbPlayer: ", len(data["metadata"]["participants"]))
print("GameTime: ", f"{info["gameDuration"]//60}:{info["gameDuration"]%60}")
print("Win: ", "Victory" if user["win"] else "Defeat")
print("----")