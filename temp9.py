import pygame
import time

pygame.init()
pygame.joystick.init()

joystick = pygame.joystick.Joystick(0)
joystick.init()

rumbling = False

while True:
    pygame.event.pump()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        if not rumbling:
            joystick.rumble(1.0, 1.0, 500)
            rumbling = True
    else:
        rumbling = False

    time.sleep(0.01)