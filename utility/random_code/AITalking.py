from lib.lib import *
import ollama

def ollama_send_message(MODEL, message):
    try:
        response = ollama.chat(model=MODEL, messages=[{"role": "user", "content": message}])
        if "message" in response and "content" in response["message"]:
            return response["message"]["content"]
        else:
            return str(response)
    except Exception as e:
        print(f"An error occurred while sending message to Ollama: {e}")
        return None

prompt = """
I'm a sub asexual lesbian trans girl but dont make the main subject just take in consideration
in french, give me really spicy message, like we are in bed
make it really visual
dont write translation, dont write multiple quote, dont sign it, dont write anything dont releated to the message
write maximum 3 line
"""
MODEL = "benevolentjoker/nsfwvanessa"


    
print(prompt)
response = ollama_send_message(MODEL, prompt)
print(response)

while True:
    text = input("send: ")
    response = ollama_send_message(MODEL, text)
    print(response)