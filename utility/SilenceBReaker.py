import time
import random
import glob
import pygame
import os

sounds = glob.glob(os.path.join("C:\\Users\\Adam\\Desktop\\Shortcut\\Music\\sound", "**", "*"), recursive=True)

random.shuffle(sounds)

pygame.init()
pygame.mixer.init()

range = [5, 15] #seconde

while True:
    random.shuffle(sounds)
    for i in sounds:
        print(i)
        music = pygame.mixer.Sound(i)
        music.set_volume(1)
        canal = music.play()
        while canal.get_busy():
            time.sleep(0.1)
        time.sleep(random.randint(range[0], range[1]))