from Crate import Crate
#from Enemy import Enemy
from Player import Player
import Session
import World
#from WorldSprite import WorldSprite
import pygame
import util

size = (800, 600)

player = Player()
player.rect.topleft = [400, 100]
player.image = pygame.Surface((32,32))
player.image.fill((0,0,255))
player.rect.size = (32,32)
player.prevRect.size = (32,32)

crate = Crate()
crate.rect.topleft = [500, 200]
crate.image = pygame.Surface((24,24))
crate.image.fill((255,150,50))
crate.rect.size = (24,24)

font = pygame.font.Font(None, 32)

'''print 'init world'
world = World.World()

print 'init worldsprites'
floor = WorldSprite(0, size[1]-32, size[0], 32)
floor.image = pygame.Surface((floor.rect.width, floor.rect.height))
floor.image.fill((0,255,0))

roof = WorldSprite(0, 0, size[0], 32)
roof.image = pygame.Surface((roof.rect.width, roof.rect.height))
roof.image.fill((0,255,0))

wall = WorldSprite(64, 450, 300, 32)
wall.image = pygame.Surface((wall.rect.width, wall.rect.height))
wall.image.fill((0,255,0))

leftWall = WorldSprite(0, 32, 32, size[1]-64)
leftWall.image = pygame.Surface((leftWall.rect.width, leftWall.rect.height))
leftWall.image.fill((0,255,0))

rightWall = WorldSprite(size[0]-32, 32, 32, size[1]-64)
rightWall.image = pygame.Surface((rightWall.rect.width, rightWall.rect.height))
rightWall.image.fill((0,255,0))


print 'populate world'
world.backgrounds = [floor, leftWall, rightWall, roof, wall]
world.clips = [floor, leftWall, rightWall, roof, wall]
world.crateSpawnZones = [[100, 700, 100, 400]]
world.gravity = 2
world.mobSpawns = [[100, 100]]

print 'save world to disk'
util.toFile('test', world.toTag())'''

print 'loading world from file'
worldtag = util.fromFile('test')
world = World.readWorld(worldtag)

world.players = [player]
world.crates = [crate]
Session = Session.Session()
Session.worlds.append(world)


while 1:
    Session.update()



'''
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
        if e.type == KEYDOWN and e.key == K_g:
            for ms in world.mobSpawns:
                world.enemies.append(Enemy())
                world.enemies[-1].rect.size = (32,32)
                world.enemies[-1].rect.midtop = ms
                world.enemies[-1].image = pygame.Surface((32,32))
                world.enemies[-1].image.fill((255,0,0))
                world.enemies[-1].health = 5

    
    if pygame.time.get_ticks() > world.lastEnemySpawn + world.enemySpawnDelay:
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

'''
    