from lib.lib import *
vivid_file = r"C:\Users\Adam\AppData\Local\VIVIDSTASIS\custom_input.txt"
#////////////////////////////#
username = "Chiyo"
message = "right"
#////////////////////////////#

#obs_client = obs_start_client()

if   message.lower() in ["left",    "gauche"]:
    file_write(vivid_file, "UnknownEnum.Value_11")
    
elif message.lower() in ["right",   "droite"]:
    file_write(vivid_file, "UnknownEnum.Value_12")
    
elif message.lower() in ["up",      "haut"]:
    file_write(vivid_file, "UnknownEnum.Value_13")
    
elif message.lower() in ["down",    "bas"]:
    file_write(vivid_file, "UnknownEnum.Value_14")
    
elif message.lower() in ["confirm", "confirmer"]:
    file_write(vivid_file, "UnknownEnum.Value_4")
    
elif message.lower() in ["cancel",  "retour"]:
    file_write(vivid_file, "UnknownEnum.Value_5")
    
elif message.lower() in ["hold", "maintenir"]:
    file_write(vivid_file, "Hold")


#print(obs_client)