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
    def update(self, world):    
        if self.impactDestroy:
            collisions = Entity.update(self, world)
            for i in collisions:
                if i:
                    world.projectiles.remove(self)
            return collisions
        else:
            return Entity.update(self, world)
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
    def update(self, world):
        if Entity.update(self, world) != (False, False):
            world.projectiles.remove(self)
            world.effects.append(Explosion(self.rect.center, 100))
        else:
            if self.momentum[0] > 0:
                self.momentum[0] += 1
            elif self.momentum[0] < 0:
                self.momentum[0] -= 1
                
    def hitEnemy(self, world):
        world.projectiles.remove(self)
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
    def update(self, world):
        prevMomentum = self.momentum[0]
        collisions = Entity.update(self, world)
        if collisions == (True, False):
            if not self.hasBounced:
                self.momentum[0] = -prevMomentum
                self.hasBounced = True
            else:
                world.projectiles.remove(self)
        elif collisions != (False, False):
            
            world.projectiles.remove(self)
            
class Grenade(Projectile):
    def __init__(self, direction, pos):
        Projectile.__init__(self, pos, (16,16))
        self.image = pygame.Surface((self.rect.size))
        self.image.fill((0,100,0))
        self.momentum = [15*direction, 0]
        self.timer = 1500
        self.impactDestroy = False
        self.creationTime = pygame.time.get_ticks()
    def update(self, world):
        if pygame.time.get_ticks() > self.creationTime + self.timer:
            self.explode(world)
        else:
            prevMom = []
            for i in self.momentum:
                prevMom.append(i)
            josh = Projectile.update(self, world)
            if josh[1]:
                self.momentum[1] = -prevMom[1]*0.75
                self.momentum[0] *= 0.75
            if josh[0]:
                self.momentum[0] = -prevMom[0]*0.75

            if math.fabs(self.momentum[0]) < 0.25:
                self.momentum[0] = 0

    def hitEnemy(self, world):
        self.explode(world)
    
    def explode(self, world):
        world.projectiles.remove(self)
        world.effects.append(Explosion(self.rect.center, 100))
        