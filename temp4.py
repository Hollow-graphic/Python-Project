from lib.lib import *
from elevenlabs.client import ElevenLabs
from elevenlabs import save
import pygame
import io
import time

prompt = """
I'm a sub asexual lesbian trans girl but dont make the main subject just take in consideration
in french, give me really spicy message, like we are in bed
make it really visual
dont write translation, dont write multiple quote, dont sign it, dont write anything dont releated to the message
write maximum 3 line
"""
MODEL = "benevolentjoker/nsfwvanessa"

print(prompt)
while True:
    response = ollama_send_message(MODEL, prompt)
    print(response)

    client = ElevenLabs(api_key="e0627c9ac954b1b8d9f6c478a39402e9dedccd551337b7e757414338720f94cd")

    audio = client.text_to_speech.convert(
        voice_id="cgSgspJ2msm6clMCkdW9",
        text=response
    )

    # 🔥 convertir le generator en bytes
    audio_bytes = b"".join(audio)

    # pygame
    pygame.mixer.init()

    audio_buffer = io.BytesIO(audio_bytes)
    pygame.mixer.music.load(audio_buffer, "mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    time.sleep(300)

# prompt = """
# I'm gonna give you a topic and you as to ask me a random question about the topic
# only answer the question and nothing else.
# your message gonna be read aloud on a TTS, incliding the semicolon
# write the response
# give me a question of difficulty 
# """
# diffilculty = 1
# MODEL = "gemma3:1b"
# topic = "Moth"

# prompt += str(diffilculty) + "/10:\n" + topic

# print(prompt)
# response = ollama_send_message(MODEL, prompt)
# print(response)
