import requests
import json
from datetime import datetime
import urllib3
from pathlib import Path

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

with open("./data/lol/riot_api_key", "r", encoding="utf-8") as f:
    RIOT_API_KEY = f.read()
    
puuid = "JQa5YtgqtTkm97DiS9RNnrAWojYq6xcUMHShveWZ4MOutYl9shSnrTw-TACWpoq68z4v2cKEvr5rYA"

function_list = {"getNewMatch":0, "getCurrentMatchStat":0, "getMatchStat":1, "getMatchStatAll":0}

loop = False

def getNewMatch(getMatchStat=False):
    with open("./data/lol/match_list.json", "r", encoding="utf-8") as f:
        match_list = json.load(f)
    r = requests.get(f"https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids", headers={"X-Riot-Token": RIOT_API_KEY})
    for i in [i for i in r if i not in match_list]: 
        match_list.append(i)
        print(f"-added: {i}")
        if getMatchStat:
            getMatchStat(i)
    with open("./data/lol/match_list.json", "w", encoding="utf-8") as f:
        f.write(r.text)
    return r.text
        
def getCurrentMatchStat():
    r = requests.get("https://127.0.0.1:2999/liveclientdata/allgamedata", verify=False)
    r.raise_for_status()
    with open(f"./data/lol/match/{datetime.now().strftime('%H-%M_%d-%m-%Y')}.json", "w", encoding="utf-8") as f:
        f.write(r.text)
    print(f"match data store in: ./data/lol/match_snapshot/{datetime.now().strftime('%Y-%m-%d_%H:%M')}")
    
def getMatchStat(match_id):
    r = requests.get(f"https://europe.api.riotgames.com/lol/match/v5/matches/{match_id}", headers={"X-Riot-Token": RIOT_API_KEY})
    with open(f"./data/lol/match/{match_id}.json", "w", encoding="utf-8") as f:
        f.write(r.text)
    print(f"-Match {match_id} Stored")
def getMatchStatAll():
    with open("./data/lol/match_list.json", "r", encoding="utf-8") as f:
        match_list = json.load(f)
    al_match_list = [str(file)[15:][:-5] for file in Path("./data/lol/match").glob("*")]
    for match_id in match_list: 
        if match_id not in al_match_list: 
            print(match_id)
            getMatchStat(match_id)

getNewMatch()
getMatchStatAll()


while loop:
    for i, function in enumerate(function_list): print(f"{i}: {function}")
    a = int(input())
    
    input_list = [input(f"{i}: ") for i in range(function_list[str(list(function_list)[a])])]
    eval(f"{list(function_list)[a]}({",".join(input_list)})")
