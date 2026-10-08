from lib.lib import *
from ollama import chat
from time import sleep

MODEL = "benevolentjoker/nsfwvanessa"
messages =[
  {
    "role": "user",
    "content": "\nin french, always speak in french, dont write PS or note, make it pretty short just one phrase\navoid talking about penis or anything related to men like they dont exist\nNEVER USE EMOJI, juste write one line, one phrase\nTALK FOR THE PERSON WHO THE PREVIOUS MESSAGE WAS FOR OR A RANDOM PERSON\nALWAYS START MESSAGE WITH YOUR NAME AND WHO YOU ARE TALKING TO\ntalk like you are in a conversation"
  },
  {
    "role": "assistant",
    "content": "\nI'm Orélie, I'm a sub asexual lesbian trans girl, and never done anything intimate before. what is your name ?"
  },
  {
    "role": "assistant",
    "content": "Vanessa à Orélie, I'm vanessa"
  },
  {
    "role": "assistant",
    "content": "Lila à Oréllie, I'm Lila, qu'est ce que tu fais ce soir ?"
  },
  {
    "role": "assistant",
    "content": "Vanessa à Lila, est ce que je peux venir ?"
  },
]

lastMessage = ""
def send(model, text="", image=""):
    if text != "" or image != "":
        message = {"role": "user"}
        if text != "":
            message.update({"content": text})
        if image != "":
            message.update({"images": image})
        messages.append(message)
    response = chat(model=model, messages=messages).message.content
    lastMessage = response
    if text != "" or image != "":
        messages.pop()
    messages.append({"role": "user", "content": response})
    print(f"{model}: {response}")
    say(response)

while True:
    send(MODEL, lastMessage)
    sleep(5)