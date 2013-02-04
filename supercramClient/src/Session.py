'''
Session Superclass
'''

import const
import pygame
import sys
from pygame.locals import *

class Session():
    def __init__(self):
        
        self.mode = 0
        '''
        0 - Init
        1 - Menu
        2 - Playing
        3 - Paused
        '''
        self.worlds = []
        self.activeWorld = 0
        
        self.screen = pygame.display.set_mode((800,600))
        self.screen.set_caption('SuperCram')
        self.clock = pygame.time.Clock()
        self.font32 = pygame.font.Font(None, 32)
        
        self.displayFPSCounter = False
    
    def update(self):
        world = self.worlds[self.activeWorld]
        
        world.buildDrawList()
        world.buildEntList()
        
        self.screen.fill(const.white)
        world.draw()
        
        if self.displayFPSCounter:
            fps = str(int(round(self.clock.get_fps())))
            fpsSurf = self.font32.render(fps, True, (0,0,0))
            fpsRect = fpsSurf.get_rect()
            fpsRect.topleft = [10,10]
            self.screen.blit(fpsSurf, fpsRect)
            
        world.eList = pygame.event.get()
        for e in world.eList:
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if e.type == QUIT:
                pygame.quit()
                sys.exit()
                
        for ls in world.entList:
            for obj in ls:
                obj.update(world)
                
        pygame.display.update()
        self.clock.tick(40)
        
        
        
        