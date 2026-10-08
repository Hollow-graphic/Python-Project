import pygame
import time
import glob
import os
import random

pygame.init()
pygame.mixer.init()

dir = r"C:\Users\Adam\Desktop\Shortcut\Music\audio"
# dir = r"C:\Users\Adam\Desktop\Shortcut\Music\audio\temp"
music_files = glob.glob(os.path.join(dir, "*"))

while True:
    random.shuffle(music_files)
    for i in music_files:
        print(i)
        music = pygame.mixer.Sound(i)
        music.set_volume(0.15)
        canal = music.play()
        while canal.get_busy():
            time.sleep(0.01)