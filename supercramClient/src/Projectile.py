'''
Projectile subclass extends Entity
'''
from Entity import Entity
from Effect import Explosion
import pygame, math

class Projectile(Entity):
    def __init__(self, pos, size):
        Entity.__init__(self)
        self.rect.size = size
        self.rect.center = pos
        self.damage = 0
        self.effectTravel = None
        self.effectCollision = None
        self.playerInteract = False
        self.timer = 0
        self.creationTime = 0
        self.impactDestroy = True
        self.enemyImpactDestroy = True #Projectile is destroyed on contatct with enemies
    def update(self, session):    
        if self.impactDestroy:
            collisions = Entity.update(self, session.worlds[session.activeWorld])
            for i in collisions:
                if i:
                    session.worlds[session.activeWorld].projectiles.remove(self)
            return collisions
        else:
            return Entity.update(self, session.worlds[session.activeWorld])
    def hitEnemy(self, world):
        pass

class Bullet(Projectile):
    def __init__(self, direction, pos):
        Projectile.__init__(self, pos, (8,8))
        self.gravity = False
        self.image = pygame.Surface((8,8))
        self.image.fill((255,200,0))
        self.damage = 1
        self.momentum = [16*direction, 0]
        
class Rocket(Projectile):
    #Sometimes not created properly
    def __init__(self, direction, pos):
        Projectile.__init__(self, pos, (32,16))
        self.gravity = False
        self.image = pygame.Surface((32,16))
        self.image.fill((0,0,0))
        self.momentum = [5*direction, 0]
    def update(self, session):
        if Entity.update(self, session.worlds[session.activeWorld]) != (False, False):
            session.worlds[session.activeWorld].projectiles.remove(self)
            session.worlds[session.activeWorld].effects.append(Explosion(self.rect.center, 100))
        else:
            if self.momentum[0] > 0:
                self.momentum[0] += 1
            elif self.momentum[0] < 0:
                self.momentum[0] -= 1
    def hitEnemy(self, world):
        world.effects.append(Explosion(self.rect.center, 100))

class Disk(Projectile):
    def __init__(self, direction, pos):
        Projectile.__init__(self, pos, (32, 8))
        self.gravity = False
        self.image = pygame.Surface((self.rect.size))
        self.image.fill((0,0,0))
        self.damage = 10
        self.momentum = [15*direction, 0]
        self.playerInteract = True
        self.hasBounced = False
        self.enemyImpactDestroy = False
    def update(self, session):
        prevMomentum = self.momentum[0]
        collisions = Entity.update(self, session.worlds[session.activeWorld])
        if collisions == (True, False):
            if not self.hasBounced:
                self.momentum[0] = -prevMomentum
                self.hasBounced = True
            else:
                session.worlds[session.activeWorld].projectiles.remove(self)
        elif collisions != (False, False):
            
            session.worlds[session.activeWorld].projectiles.remove(self)
            
class Grenade(Projectile):
    def __init__(self, direction, pos, yMom):
        Projectile.__init__(self, pos, (16,16))
        self.image = pygame.Surface((self.rect.size))
        self.image.fill((0,100,0))
        self.momentum = [18*direction, yMom*1.5]
        self.timer = 1500
        self.impactDestroy = False
        self.creationTime = pygame.time.get_ticks()
    def update(self, session):
        if pygame.time.get_ticks() > self.creationTime + self.timer:
            self.explode(session.worlds[session.activeWorld])
            session.worlds[session.activeWorld].projectiles.remove(self)
        else:
            prevMom = []
            for i in self.momentum:
                prevMom.append(i)
            collisions = Projectile.update(self, session)
            if collisions[1]:
                self.momentum[1] = -prevMom[1]*0.6
                self.momentum[0] *= 0.75
            if collisions[0]:
                self.momentum[0] = -prevMom[0]*0.6
            if math.fabs(self.momentum[0]) < 0.25:
                self.momentum[0] = 0

    def hitEnemy(self, world):
        self.explode(world)
    
    def explode(self, world):
        world.effects.append(Explosion(self.rect.center, 100))
        