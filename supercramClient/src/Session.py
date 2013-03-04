'''
Session Superclass
'''

from pygame.locals import *
import const
import Enemy
import pygame
import sys
import time
import random

class Session():
    def __init__(self):
        
        self.mode = 2
        '''
        0 - Init
        1 - Menu
        2 - Playing
        3 - Multiplayer
        4 - Paused
        5 - Game Over
        '''
        self.worlds = []
        self.activeWorld = 0
        self.multiplayer = False
        
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption('SuperCram')
        self.clock = pygame.time.Clock()
        self.font32 = pygame.font.Font(None, 32)
        
        self.displayFPSCounter = False
        self.devCon = False
        
        self.spawnEnemies = True
        self.spawnCrates = True
        
        
    def update(self):
        if self.mode == 2:
            world = self.worlds[self.activeWorld]
            time = pygame.time.get_ticks()
            
            world.buildEntList()
            
            self.screen.fill(const.white)
            world.draw(self.screen)
            
            if self.displayFPSCounter:
                fps = str(int(round(self.clock.get_fps())))
                fpsSurf = self.font32.render(fps, True, (0,0,0))
                fpsRect = fpsSurf.get_rect()
                fpsRect.topleft = [10,10]
                self.screen.blit(fpsSurf, fpsRect)
                
            if self.spawnEnemies:
                if time > world.lastEnemySpawn + world.enemySpawnDelay:
                    for spawn in world.mobSpawns:
                        world.enemies.append(Enemy.Enemy(random.choice(const.enemyParams), spawn))
                        world.lastEnemySpawn = time
            
                
            world.eList = pygame.event.get()
            for e in world.eList:
                if e.type == KEYDOWN:
                    if e.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif e.key == K_p:
                        time.sleep(2)
                if e.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    
            for ls in world.entList:
                for obj in ls:
                    obj.update(self)
                    
            pygame.display.update()
            self.clock.tick(40)

        
        
        