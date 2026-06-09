import asyncio
import websockets
import json
import uuid
import time

# CONFIG
SERVER = "ws://localhost:38281"  # ou serveur distant
SLOT_NAME = "Temp49"               # nom exact du slot dans la seed
GAME = "Celeste 64"

async def send_deathlink(ws, cause="Python DeathLink test"):
    """Envoie un DeathLink au serveur"""
    packet = [{
        "cmd": "Bounce",
        "tags": ["DeathLink"],
        "data": {
            "time": time.time(),
            "source": SLOT_NAME,
            "cause": cause
        }
    }]
    print("SEND DeathLink:", packet)
    await ws.send(json.dumps(packet))


async def connect():
    async with websockets.connect(SERVER) as ws:
        print("Connecté au serveur")

        # Recevoir RoomInfo
        msg = await ws.recv()
        print("RECV RoomInfo:", msg)

        # Demander DataPackage
        await ws.send(json.dumps([{
            "cmd": "GetDataPackage",
            "games": [GAME]
        }]))
        msg = await ws.recv()
        print("RECV DataPackage:", msg)
        # add all the id of item_name_to_id in a list
        msg = json.loads(msg)
        item_ids = list(msg[0]["data"]["games"]["Celeste 64"]["item_name_to_id"].values())
        print("Item IDs:", item_ids)
        open("./Archipelago/item_ids.txt", "w").write("\n".join(str(id) for id in item_ids))
        # chose random task in task_list.txt and associate it with a random item id
        task_list = open("./Archipelago/task_list.txt").read().splitlines()
        for task in task_list:
            item_id = item_ids.pop(0)  # get the first item id and remove it from the list
            print(f"Task: {task} - Item ID: {item_id}")
            open("./Archipelago/task_item_mapping.txt", "a").write(f"{task}: {item_id}\n")

asyncio.run(connect())
