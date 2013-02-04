import pygame
from pygame.locals import *
pygame.init()

def init(a):
    screen = pygame.display.set_mode(a)
    pygame.display.set_caption('Super Cram Box')

    return screen
