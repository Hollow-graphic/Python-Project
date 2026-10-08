import socket
import asyncio
import edge_tts
import pygame
import queue
import threading
import uuid
import os
import random


# File d'attente des messages Twitch
messages = queue.Queue()

voice_list = [
    "en-AU-NatashaNeural",
    "en-AU-WilliamMultilingualNeural",
    "en-CA-ClaraNeural",
    "en-CA-LiamNeural",
    "en-GB-LibbyNeural",
    "en-GB-RyanNeural",
    "en-GB-SoniaNeural",
    "en-GB-ThomasNeural",
    "en-HK-SamNeural",
    "en-HK-YanNeural",
    "en-IE-ConnorNeural",
    "en-IE-EmilyNeural",
    "en-IN-NeerjaExpressiveNeural",
    "en-IN-NeerjaNeural",
    "en-IN-PrabhatNeural",
    "en-KE-AsiliaNeural",
    "en-KE-ChilembaNeural",
    "en-NG-AbeoNeural",
    "en-NG-EzinneNeural",
    "en-NZ-MitchellNeural",
    "en-NZ-MollyNeural",
    "en-PH-JamesNeural",
    "en-PH-RosaNeural",
    "en-SG-LunaNeural",
    "en-SG-WayneNeural",
    "en-TZ-ElimuNeural",
    "en-TZ-ImaniNeural",
    "en-US-AndrewMultilingualNeural",
    "en-US-AndrewNeural",
    "en-US-AriaNeural",
    "en-US-AvaMultilingualNeural",
    "en-US-AvaNeural",
    "en-US-BrianMultilingualNeural",
    "en-US-BrianNeural",
    "en-US-ChristopherNeural",
    "en-US-EmmaMultilingualNeural",
    "en-US-EmmaNeural",
    "en-US-EricNeural",
    "en-US-GuyNeural",
    "en-US-JennyNeural",
    "en-US-MichelleNeural",
    "en-US-RogerNeural",
    "en-US-SteffanNeural",
    "en-ZA-LeahNeural",
    "en-ZA-LukeNeural"
]

async def create_tts(text, filename):
    voice = random.choice(voice_list)
    print(f"-- {voice}")
    await edge_tts.Communicate(
        text,
        voice
    ).save(filename)


def speak(text):
    filename = f"tts_{uuid.uuid4()}.mp3"

    asyncio.run(create_tts(text, filename))

    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.wait(100)

    pygame.mixer.quit()

    os.remove(filename)


def tts_worker():
    while True:
        msg = messages.get()
        try:
            speak(msg)
        except Exception as e:
            print("Erreur TTS :", e)

pseudo_money = {}

def message_manager(pseudo, message):
    return messages

# Thread qui lit les messages TTS
threading.Thread(target=tts_worker, daemon=True).start()


# Connexion Twitch IRC
server = "irc.chat.twitch.tv"
port = 6667

channel = "dougdoug"  # chaîne Twitch à écouter

sock = socket.socket()
sock.connect((server, port))

sock.send(b"PASS SCHMOOPIIE\r\n")
sock.send(b"NICK justinfan12345\r\n")
sock.send(f"JOIN #{channel}\r\n".encode())


print(f"Connecté au chat de {channel}")


while True:
    data = sock.recv(2048).decode("utf-8", errors="ignore")

    for line in data.split("\r\n"):

        if line.startswith("PING"):
            sock.send("PONG :tmi.twitch.tv\r\n".encode())

        elif "PRIVMSG" in line:
            msg = line.split(":", 2)[-1].strip()
            pseudo = line.split("!")[0][1:]

            if msg.startswith("We have a Minecraft server for Subscribers"):
                continue

            if msg:
                messages = message_manager(pseudo, messages)
                print(f"{pseudo}: {msg}")
                messages.put(msg)
            if msg.startswith("Cheer"):
                pass