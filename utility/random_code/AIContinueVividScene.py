from lib.lib import *
from ollama import chat
from random import choice
from pyautogui import screenshot
from time import sleep
import json

prompt = """
you goal is to continue the scene as the caracter presented. 
more information about the character:
saturday: trans girl with a lot of trauma. girlfriend of allison
allison: orphan asexuel girl with a lot of trauma. girlfriend of satruday
narrator: its not a character but the narrator of the story
"""
MODEL = ["benevolentjoker/nsfwvanessa"]

with open("./data/vivid_.json", "r", encoding="utf-8") as f:
    messages = json.load(f)

def send(model, text="", image=""):
    if text != "" or image != "":
        message = {"role": "user"}
        if text != "":
            message.update({"content": text})
        if image != "":
            message.update({"images": image})
        messages.append(message)
    response = chat(model=model, messages=messages).message.content
    messages.pop()
    messages.append({"role": "assistant/"+model, "content": response})
    print(f"{model}: {response}")
    with open("./data/vivid_.json", "w", encoding="utf-8") as f:
        json.dump(messages, f, ensure_ascii=False, indent=2)
    say(response)

while True:
    model = MODEL[0] #choice(MODEL)
    send(model, prompt)
    sleep(5)