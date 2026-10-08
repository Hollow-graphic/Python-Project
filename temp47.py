import json
from pathlib import Path


def getMatchStatAll():
    with open("./data/lol/match_list.json", "r", encoding="utf-8") as f:
        match_list = json.load(f)
    al_match_list = [str(file)[15:][:-5] for file in Path("./data/lol/match").glob("*")]

    for match_id in match_list: 
        if match_id not in al_match_list: 
            print(match_id)
            getMatchStat(match_id)

getMatchStatAll()