import requests
import json
import os

url = "https://gamebanana.com/mods/709663"
mod_id = url[-6:]
print(mod_id)

def fetch_url(url):
    response = requests.get(url)
    response.raise_for_status()
    return response

data = fetch_url(f"https://gamebanana.com/apiv8/Mod/{mod_id}?_csvProperties=_idRow,_sName,_aFiles").text
print(data)
data = json.loads(data)

dl_id = data["_aFiles"][0]["_sDownloadUrl"].split("/")[-1]

os.startfile(f"everest:https://gamebanana.com/dl/{dl_id}?")


