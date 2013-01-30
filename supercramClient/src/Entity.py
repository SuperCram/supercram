'''
Entity superclass, represents all moving objects on-screen
'''
import pygame
pygame.init()

class Entity():
    def __init__(self):
        self.momentum = [0,0]
        self.image = ''
        self.clipping = True
        self.gravity = True
        self.deleted = False
        self.uid = 0
        self.rect = pygame.Rect((0,0), (0,0))
        self.prevRect = pygame.Rect([0,0], (0,0))

    def update(self, world):
   
        if self.gravity:
            self.momentum[1] += world.gravity

        if self.momentum != [0,0]:
            #Move prevRect before updating location
            self.prevRect.topleft = self.rect.topleft
            #Update location, check collisions            
            #Horizontal
            hitH = False
            self.rect.left = (self.rect.left + self.momentum[0])
            for r in world.map:
                if self.rect.colliderect(r):
                    hitH = True
                    if self.momentum[0] > 0: #moving right
                        self.rect.right = r.rect.left
                        self.momentum[0] = 0
                    elif self.momentum[0] < 0: #moving left
                        self.rect.left = r.rect.right
                        self.momentum[0] = 0
            
            #Vertical
            hitV = False
            self.rect.top = (self.rect.top + self.momentum[1])
            for r in world.map:
                if self.rect.colliderect(r):
                    hitV = True                
                    if self.momentum[1] > 0: #moving down
                        self.rect.bottom = r.rect.top
                        self.momentum[1] = 0
                        
                    elif self.momentum[1] < 0: #moving up
                        self.rect.top = r.rect.bottom
                        self.momentum[1] = 0
        return (hitH, hitV)

        #Will be overridden/extended by subclasses
    
    def remove(self):
        #Does things probs
        pass
    