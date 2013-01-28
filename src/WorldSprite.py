'''
WorldSprite superclass, represents world collision boxes, trigger zones
'''
import pygame

class WorldSprite():
    def __init__(self, left, top, width, height):
        self.collisions = 1
        self.background = True
        self.image = ''
        self.rect = pygame.Rect(left, top, width, height)
        