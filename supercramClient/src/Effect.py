'''
Effect superclass
'''
import pygame, const

class Effect():
    def __init__(self, pos, startTime):
        self.pos = pos
        self.image = ''
        self.enemyInteract = False
        self.playerInteract = False
        self.damage = 0
        self.startTime = startTime
        self.life = 0

###################################
class Explosion(Effect):
    def __init__(self, pos, radius):
        Effect.__init__(self, pos, pygame.time.get_ticks())
        self.radius = radius
        self.image = pygame.Surface((self.radius*2, self.radius*2))
        self.image.set_colorkey((0,0,0))
        self.rect = pygame.draw.circle(self.image, (255,0,255), (self.radius, self.radius), self.radius)
        self.rect.center = pos
        self.enemyInteract = True
        self.damage = 100
        self.startTime = pygame.time.get_ticks()
        self.life = 100
    def update(self, session):
        now = pygame.time.get_ticks()
        if now > self.startTime + self.life:
            session.worlds[session.activeWorld].effects.remove(self)
        else:
            for enemy in session.worlds[session.activeWorld].enemies:
                if const.distance(self.pos, enemy.rect.center) < self.radius:
                    enemy.health -= self.damage