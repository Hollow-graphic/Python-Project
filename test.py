from lib.lib import *
import time
import configparser
import pygame

config = configparser.ConfigParser()
config.read("config.ini")
vivid_file = r"C:\Users\Adam\AppData\Local\VIVIDSTASIS\custom_input.txt"
cc_file = r"C:\Users\Adam\AppData\Roaming\PrismLauncher\instances\FastStartup\minecraft\saves\CC_tweak\computercraft\computer\0\text.txt"
current_game = "vivid"

#obs_client = obs_start_client()
#pygame.mixer.init()

#////////////////////////////#
username = "Chiyo"
message = "yippie"
#////////////////////////////#







VTC = int((time.time() - 946684790)/1850)
print(f"VTC: {VTC}")