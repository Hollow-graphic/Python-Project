import pytchat
from lib.lib import *
import random
import time
import configparser
import pygame
pygame.mixer.init()
import pyttsx3
echo = True

config = configparser.ConfigParser()
config.read("config.ini")
vivid_file = r"C:\Users\Adam\AppData\Local\VIVIDSTASIS\custom_input.txt"
mc_save = ""
cc_file = r"C:\Users\Adam\AppData\Roaming\PrismLauncher\instances\Archipelago Fabric Only\minecraft\saves\{mc_save}\computercraft\computer\0\text.txt"
message_list = []

sound_dir = r"C:\Users\Adam\Desktop\Shortcut\Music\sound"
list = os.listdir(sound_dir)
for i in range(len(list)):
    list[i] = list[i][:-4]

#////////////////////////////#
video_id = ""
current_game = ["vivid", "minecraft"]
#////////////////////////////#

if not video_id:
    video_id = input("Stream ID: ")
    
chat = pytchat.create(video_id=video_id)
obs_client = obs_start_client()

def message_manager(username, message):
    username = username[1:]
    global current_game
    
    if len(message) >= 94:
        print("!message to long")
        return
    if message.startswith("/"):
        message = "!" + message[1:]
    if username == "HollowetNini":
        if message.startswith("!game"):
            message = message[6:]
            if message.startswith("add"):
                current_game.append(message[4:])
            if message.startswith("rem"):
                message = message[4:]
                for i  in range(len(current_game)):
                    if message == current_game[i]:
                        current_game.remove(current_game[i])
                        break
            print(f'game changed to {current_game}')
            return
        if message.startswith("!mc"):
            mc_save = message[4:]
            if "minecraft" not in current_game:
                current_game.append("minecraft")
            return
        if message.startswith("!live"):
            global chat 
            chat = pytchat.create(video_id=message[6:])
            return
    if message.startswith("!color"):
        color = message[6:]
        if " " not in message:
            message = f"{message}, {message}"
        if not "," in color:
            color = color.replace(" ", ", ")
        if not config.has_section(username):
            config.add_section(username)
        config[username]["color"] = color
        with open("config.ini", "w") as f:
            config.write(f)
        return
    if message.lower() in list:
        print(f"play sound: {message.lower()}.mp3")
        pygame.mixer.music.load(os.path.join(sound_dir, message.lower()+".mp3"))
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
        return
    if "vivid" in current_game:
        if   message.lower() in ["left",    "gauche"]:
            file_write(vivid_file, "UnknownEnum.Value_11")
            return
        elif message.lower() in ["right",   "droite"]:
            file_write(vivid_file, "UnknownEnum.Value_12")
            return
        elif message.lower() in ["up",      "haut"]:
            file_write(vivid_file, "UnknownEnum.Value_13")
            return
        elif message.lower() in ["down",    "bas"]:
            file_write(vivid_file, "UnknownEnum.Value_14")
            return
        elif message.lower() in ["confirm", "confirmer"]:
            file_write(vivid_file, "UnknownEnum.Value_4")
            return
        elif message.lower() in ["cancel",  "retour"]:
            file_write(vivid_file, "UnknownEnum.Value_5")
            return
        elif message.lower() in ["hold", "maintenir"]:
            file_write(vivid_file, "Hold")
            return
    
    color = config.get(username, "color", fallback=None)
    if not color:
        color = f"{random_color()}, {random_color()}"
        
    character = username
    file = r".\web\custom_character\assets\sp_u_" + username.lower() + ".png"
    if not os.path.exists(file):
        character = str(randint(0,5))

    obs_hide(obs_client, "_VividChat", 1, True)
    obs_hide(obs_client, "_VividChat", 2, True)

    file_write(live_username, username)
    file_write(live_message, message)
    file_write(live_color, color)
    file_write(live_character, character)
    
    obs_refresh_web(obs_client, "textbox")
    obs_refresh_web(obs_client, "character")
    
    engine = pyttsx3.init()
    engine.setProperty("volume", 1.0) # volume (0.0 à 1.0)
    engine.say(message)
    engine.runAndWait()
    
    time.sleep(5)
    obs_hide(obs_client, "_VividChat", 1, False)
    obs_hide(obs_client, "_VividChat", 2, False)

while chat.is_alive():
    for c in chat.get().sync_items():
        print(f"[{c.datetime}] {c.author.name}: {c.message}")
        #message_list.append(c.message)
        message_manager(c.author.name, c.message)
        