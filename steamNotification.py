import steam
import asyncio
import websockets
import json
import os
import math
import yaml
#Dont use emojis in the code, my font cant display them

account_file = "data/account.txt"
options_file = "data/options.yaml"
slot_file = "data/slots.txt"
agenda_file = "data/agenda.txt"
account = open(account_file, "r").read().splitlines()
Options = yaml.safe_load(open(options_file, "r"))
SLOTS = open(slot_file, "r").read().splitlines()
SERVER = account[2]
has_agenda = False
last_command = None

pi = 3.141592653589793238462643383

class MyClient(steam.Client):
    async def on_ready(self):
        print(f"Steam Bot connected : {self.user}")
        self.receiver = await self.fetch_user(int(account[3]))
        asyncio.create_task(self.console())

    async def console(self):
        global SLOTS, SERVER, has_agenda, last_command
        loop = asyncio.get_event_loop()
        while True:
            cmd = await loop.run_in_executor(None, input, "> ")
            if cmd.startswith("/"):
                cmd = cmd[1:]
            if cmd.startswith("archipelago"): #Achipelago commands
                if cmd.startswith("archipelago server"):
                    parts = cmd.split(" ", 2)
                    if len(parts) < 3 or not parts[2]:
                        print(f"Serveur actuel : {SERVER}")
                    else:
                        SERVER = parts[2]
                        open(account_file, "w").write(f"{account[0]}\n{account[1]}\n{SERVER}\n{account[3]}")
                        print(f"Serveur changé : {SERVER}")

                elif cmd.startswith("archipelago add "):
                    slot = cmd.split(" ", 2)[2]
                    SLOTS.append(slot)
                    open(slot_file, "w").write("\n".join(SLOTS))
                    asyncio.create_task(self.listen_archipelago(slot))
                    print(f"Slot ajouté : {slot}")

                elif cmd.startswith("archipelago remove "):
                    slot = cmd.split(" ", 2)[2]
                    if slot in SLOTS:
                        SLOTS.remove(slot)
                        open(slot_file, "w").write("\n".join(SLOTS))
                        print(f"Slot supprimé : {slot} (sera déconnecté au prochain cycle)")
                    else:
                        print(f"Slot introuvable : {slot}")

                elif cmd == "archipelago list":
                    print(f"Serveur : {SERVER}")
                    print(f"Slots : {SLOTS}")

                elif cmd == "archipelago connect":
                    print(f"Connexion à {SERVER} pour {SLOTS}")
                    for slot in SLOTS:
                        asyncio.create_task(self.listen_archipelago(slot))
                        
                elif cmd == "archipelago slots":
                    print(f"Slots actuels : {SLOTS}")
            elif cmd[0] in '=0123456789': #calculator 
                if cmd[0] == "=":
                    cmd = cmd[1:]
                try: #cmd.startswith("=") or 
                    result = eval(cmd) #result = eval(cmd[1:])
                    print(f"→ {result}")
                except Exception as e:
                    print(f"Erreur de calcul : {e}")
            elif cmd.startswith("agenda"):
                if cmd.startswith("agenda add "):
                    open(agenda_file, "a").write(cmd.split(" ", 2)[2] + "\n")
                    print("Agenda Updated")
                    has_agenda = True
                elif cmd.startswith("agenda verify"):
                    print("Done")
                    has_agenda = True
            elif cmd == "shutdown" or cmd == "xda": #Shutdown The bot
                if not has_agenda:
                    print("Finish Agenda before shutdown")
                else:
                    if last_command == "shutdown" or last_command == "xda":
                        last_command = None
                        os.system("shutdown /s /t 5")
                        print("Shutdown de l'apareil dans 5 secondes...")
                    else:
                        print("Sure ?")
            elif cmd == "restart": #Restart The bot
                print("Redémarrage du bot...")
                await self.close()
                os._exit(0)
            elif cmd == "help":
                if cmd == "help archipelago":
                    print("/archipelago server <adresse:port>  → changer le serveur")
                    print("/archipelago add <slot>             → ajouter un slot")
                    print("/archipelago remove <slot>          → supprimer un slot")
                    print("/archipelago list                   → voir la config actuelle")
                    print("/archipelago connect                → se reconnecter a tous les slots")
                else:
                    print("/archipelago ...")
                    print("/restart                            → redemarrer le bot")
            last_command = cmd
    async def listen_archipelago(self, slot: str):
        global SERVER
        if slot not in SLOTS or not Options["steam"]:
            print(f"[{slot}] Slot supprimé, arrêt")
            return
        try:
            first_items = True
            async with websockets.connect(f"ws://{SERVER}") as ws:
                print(f"[{slot}] Connecté à Archipelago")
                await ws.send(json.dumps([{
                    "cmd": "Connect",
                    "name": slot,
                    "game": "",
                    "password": "",
                    "uuid": f"steambot_{slot}",
                    "version": {"major": 0, "minor": 5, "build": 0, "class": "Version"},
                    "items_handling": 0b111,
                    "tags": ["TextOnly"],
                }]))

                async for message in ws:
                    if slot not in SLOTS:
                        break
                    packets = json.loads(message)
                    for packet in packets:
                        if packet["cmd"] == "ReceivedItems":
                            if first_items:
                                first_items = False
                                continue
                            await self.receiver.send(f"[{slot}] Tu as reçu un item !")
                        if packet["cmd"] == "PrintJSON":
                            texte = "".join(p.get("text", "") for p in packet.get("data", []))
                            if "hint" in texte.lower():
                                await self.receiver.send(f"[{slot}] Hint : {texte}")

        except Exception as e:
            print(f"[{slot}] Déconnecté : {e}")

client = MyClient()
client.run(account[0], account[1])