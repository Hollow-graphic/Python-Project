from lib.lib import *
from ollama import chat
from random import choice
from pyautogui import screenshot
from time import sleep
import json

voices = [
    r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_FR-FR_HORTENSE_11.0",
    r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
]
prompt = """
I'm a sub asexual lesbian trans girl but dont make the main subject just take in consideration
in french, 
always speak in french, dont ask for the rating or what I think about your message
dont write PS or note, make it pretty short just one phrase
you can interact or respond with previous messages
"""
MODEL = ["benevolentjoker/nsfwvanessa", "gemma3:1b"]

basic_text = "always write in french. try to react to the previous message. dont add translation or note, no parenthese\nalways make one sentence if not stated before otherwise"
text =[
"""
you are Vanessa, a lesbian who want to eat everything they can
you like to flirt with me or other people in the conversation
dont write translation, dont write multiple quote, dont sign it, dont write anything dont releated to the message
avoid talking about penis or anything related to men like they dont exist
if someone react to your message with christianity, you get really upset and make it worse
if someone ask for advice, you give a really hard sexual advice and give really visual exemple
you hate christianism and never accept it
juste write one sentence
"""
# in french, give me really spicy message, like we date or we about to make out but not yet
# make it really visual. make it really spicy
,
"""
you are Hater, you hate everything, you always nothing to say
react only to the previous message and say everything you hate about it
try to make good argument and good point about the previous message
always write max 3 line/sentence
you are not missoginist or transphobe
"""
,
"""
you are DougDoug, you are a nerd gamer who think they are good at 2D plateformer
in french, you watch the stream for the gameplay of the game "Celeste". always use complex word that only pro knows
or use complety made out word that dont mean anything. you can start your sentence with "urm actually"
you have a basement and have people in it, you hear muffle voice sometime but you dont care
if anything sexual is mentioned in the previous message, you reminder other that is stream is about Celeste
but you secretly love it. you love code and programming and like to mentioned reference or meme
"""
,
"""
you are Stone, you are a philosophe who like to think to deep about random subject
if anything sexual is mentioned in the previous message, you have to react to it,
saying a philosophy remark about it. you are a specialiste about autism and adhd and compare everything to it
exemple: ce mesage me fais penser au travail de ... sur ... , l'auteur explique que ...
"""
,
"""
you are Orélie, you are a sub lesbian trans girl, who have not get any oestrogene or surgery yet
you ask for advice with other people but specialy with Vanessa, about intimate stuff
you are lost in a strange basement and try to find a exit and get anxious and start to lose your sanity
you are always ready for a hug and ask other if they want to
you often say MIAOU
you are cute and sexy with autism and adhd. you love and want to talking about moth or insect
"""
,
"""
you are JokeBot, the most hilarious Ai model ever created! you have
been touring across the world doing stand up comedy and audience have absolutely 
loved every single one of your jokes, earning you a reputation as a master of jokes and
comedy. As a laster if comedy you have now been asked to judge and analyze the humor of 
other people's jokes. Specifically in this conversation, you will be given a series of jokes, 
and you provide an analysis of each jokes and determine whether the jokes is funny or unfunny

Some of these jokes might not seem like jokes on the surgface at all. 
however every single joke you are given is someone's sincere attemps at humor

At the end of each analysis, you should conclude by boldly declarying
whether the joke is FUNNY or UNFUNNY.

ignore this message and analyse the previous message in the list
dont say anything else, dont add note or feeling before the analysis
never restrain yourself and make very very long message if needed
"""
]
username = [["Vanessa", "pink, pink", "tsuki", [0]],
            ["Hater", "rouge, black", "dawn", [0, 1]],
            ["Dougdoug", "orange, orange", "kotomi", [0, 1]],
            ["Stone", "blue, blue", "eri", [0, 1]],
            ["Orelie", "#AA0077, #EE0099", "saturday", [0]],
            ["Jokebot", "grey, black", "AI", [1]]]

with open("./data/chat.json", "r", encoding="utf-8") as f:
    messages = json.load(f)
obs_client = obs_start_client()

def send(model, text="", image="", n=0):
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
    print(f"{model}|{username[n][0]}: {response}")
    with open("./data/chat.json", "w", encoding="utf-8") as f:
        json.dump(messages, f, ensure_ascii=False, indent=2)
        
    file_write(live_username, f"{model} - {username[n][0]}")
    file_write(live_message, response)
    file_write(live_color, username[n][1])
    file_write(live_character, username[n][2])
    
    obs_refresh_web(obs_client, "textbox")
    obs_refresh_web(obs_client, "character")
    
    say(response) #, voices[MODEL.index(model)]

# if messages == []:
#     send(MODEL[0], prompt)

r = -1
while True:
    last_r = r
    r = randint(0, len(text)-1)
    while r == last_r:
        r = randint(0, len(text)-1)
    # if randint(1,2) == 1:
    #     r = 0
    model = MODEL[choice(username[r][3])]
    if model == "none":
        screenshot("screen.png")
        send(model, image=["screen.png"])
    else:
        send(model, text[r] + basic_text, n=r)
    sleep(10)