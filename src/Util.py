import pygame
from pygame.locals import *
pygame.init()

def init(a):
    screen = pygame.display.set_mode(a)
    pygame.display.set_caption('Super Cram Box')

    return screen
def eventList(keysDown):
    eLs = pygame.event.get()
    for e in eLs:
        if e.type == KEYDOWN:
            if e.key not in keysDown:
                keysDown.append(e.key)
        elif e.type == KEYUP:
            if e.key in keysDown:
                keysDown.remove(e.key)
                
    return eLs, keysDown