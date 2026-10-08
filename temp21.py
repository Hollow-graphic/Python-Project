import os
import yaml

#Dont use emojis in the code, my font cant display them

account_file = "data/account.txt"
options_file = "data/options.yaml"
slot_file = "data/slots.txt"
agenda_file = "data/agenda.txt"


def read_lines(path):
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return f.read().splitlines()


def read_yaml(path):
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def safe_input(prompt):
    try:
        return input(prompt)
    except (EOFError, KeyboardInterrupt):
        return ""


account = read_lines(account_file)
Options = read_yaml(options_file)
SLOTS = read_lines(slot_file)
SERVER = account[2] if len(account) > 2 else ""
has_agenda = False
last_command = None

while True:
    cmd = input()
    if not cmd:
        continue
    if cmd.startswith("/"):
        cmd = cmd[1:]
    if cmd.startswith("archipelago"): #Achipelago commands
        if cmd.startswith("archipelago server"):
            parts = cmd.split(" ", 2)
            if len(parts) < 3 or not parts[2]:
                print(f"Serveur actuel : {SERVER}")
            else:
                SERVER = parts[2]
            with open(account_file, "w", encoding="utf-8") as f:
                f.write(f"{account[0]}\n{account[1]}\n{SERVER}\n{account[3]}")
            print(f"Serveur changé : {SERVER}") 
        elif cmd.startswith("archipelago add "):
            slot = cmd.split(" ", 2)[2]
            SLOTS.append(slot)
            with open(slot_file, "w", encoding="utf-8") as f:
                f.write("\n".join(SLOTS))
            #asyncio.create_task(listen_archipelago(slot))
            print(f"Slot ajouté : {slot}")  
        elif cmd.startswith("archipelago remove "):
            slot = cmd.split(" ", 2)[2]
            if slot in SLOTS:
                SLOTS.remove(slot)
                with open(slot_file, "w", encoding="utf-8") as f:
                    f.write("\n".join(SLOTS))
                print(f"Slot supprimé : {slot} (sera déconnecté au prochain cycle)")
            else:
                print(f"Slot introuvable : {slot}") 
        elif cmd == "archipelago list":
            print(f"Serveur : {SERVER}")
            print(f"Slots : {SLOTS}")   
        elif cmd == "archipelago connect":
            print(f"Connexion à {SERVER} pour {SLOTS}")
            for slot in SLOTS:
                #asyncio.create_task(self.listen_archipelago(slot))
                pass

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
            with open(agenda_file, "a", encoding="utf-8") as f:
                f.write(cmd.split(" ", 2)[2] + "\n")
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
        os._exit(0)
    elif cmd == "help":
        if cmd == "help archipelago" or "archipelago help" or "archipelago ?":
            print("/archipelago server <adresse:port>  → changer le serveur")
            print("/archipelago add <slot>             → ajouter un slot")
            print("/archipelago remove <slot>          → supprimer un slot")
            print("/archipelago list                   → voir la config actuelle")
            print("/archipelago connect                → se reconnecter a tous les slots")
        else:
            print("/archipelago ...")
            print("/restart                            → redemarrer le bot")
    last_command = cmd