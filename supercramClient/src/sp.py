from Crate import Crate
from Enemy import Enemy
from Player import Player
from World import World
from WorldSprite import WorldSprite
from pygame.locals import *
import Util
import pygame
import sys


screen = Util.init((800, 600))
clock = pygame.time.Clock()

player = Player()
player.rect.topleft = [400, 100]
player.image = pygame.Surface((32,32))
player.image.fill((0,0,255))
player.rect.size = (32,32)
player.prevRect.size = (32,32)

enemy = Enemy()
enemy.rect.topleft = [100, 100]
enemy.image = pygame.Surface((32,32))
enemy.image.fill((255,0,0))
enemy.rect.size = (32,32)
enemy.prevRect.size = enemy.rect.size
enemy.health = 5

crate = Crate()
crate.rect.topleft = [500, 200]
crate.image = pygame.Surface((24,24))
crate.image.fill((255,150,50))
crate.rect.size = (24,24)

font = pygame.font.Font(None, 32)

world = World()
world.size = (800,600)

floor = WorldSprite(0, world.size[1]-32, world.size[0], 32)
floor.image = pygame.Surface((floor.rect.width, floor.rect.height))
floor.image.fill((0,255,0))

roof = WorldSprite(0, 0, world.size[0], 32)
roof.image = pygame.Surface((roof.rect.width, roof.rect.height))
roof.image.fill((0,255,0))

wall = WorldSprite(64, 450, 300, 32)
wall.image = pygame.Surface((wall.rect.width, wall.rect.height))
wall.image.fill((0,255,0))

leftWall = WorldSprite(0, 32, 32, world.size[1]-64)
leftWall.image = pygame.Surface((leftWall.rect.width, leftWall.rect.height))
leftWall.image.fill((0,255,0))

rightWall = WorldSprite(world.size[0]-32, 32, 32, world.size[1]-64)
rightWall.image = pygame.Surface((rightWall.rect.width, rightWall.rect.height))
rightWall.image.fill((0,255,0))

world.map = [floor, leftWall, rightWall, roof, wall]
world.players = [player]
world.crates = [crate]
world.gravity = 2
world.mobSpawns = [[100, 100]]

for i in world.drawList:
    for e in i:
        print i.size, i.position

enemySpawn = 0
while 1:
    world.buildDrawList()
    world.buildEntList()
    
    screen.fill((255,255,255))
    world.draw(screen)
    
    fps = str(int(round(clock.get_fps())))
    fpsSurf = font.render(fps, True, (0,0,0))
    fpsRect = fpsSurf.get_rect()
    fpsRect.topleft = [10,10]
    screen.blit(fpsSurf, fpsRect)
    
    world.eList = pygame.event.get()
    
    for e in world.eList:
        if e.type == KEYDOWN and e.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
        if e.type == QUIT:
            pygame.quit()
            sys.exit()
    
    for e in world.eList:
        if e.type == KEYDOWN and e.key == K_y:
            for ms in world.mobSpawns:
                world.enemies.append(Enemy())
                world.enemies[-1].rect.size = (32,32)
                world.enemies[-1].rect.midtop = ms
                world.enemies[-1].image = pygame.Surface((32,32))
                world.enemies[-1].image.fill((255,0,0))
                world.enemies[-1].health = 5

    
    if pygame.time.get_ticks() > enemySpawn + 5000:
        print 'Enemy spawned'
        for ms in world.mobSpawns:
            world.enemies.append(Enemy())
            world.enemies[-1].rect.size = (32,32)
            world.enemies[-1].rect.midtop = ms
            world.enemies[-1].image = pygame.Surface((32,32))
            world.enemies[-1].image.fill((255,0,0))
            world.enemies[-1].health = 5
        enemySpawn = pygame.time.get_ticks()

    for ls in world.entList:
        for obj in ls:
            obj.update(world)
        
    #pygame.display.update(world.buildRectLs())
    pygame.display.update()
    clock.tick(40)
    

