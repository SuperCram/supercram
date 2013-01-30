'''
Weapon superclass
'''
import pygame, Projectile

class Weapon():
    def __init__(self):
        self.image = ''
        self.fireDelay = 0
        self.lastShot = 0
        self.rapidFire = False
    def checkReady(self):
        now = pygame.time.get_ticks()
        if now < self.lastShot + self.fireDelay:
            return False
        else:
            return True
    
class Pistol(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.fireDelay = 100
    def shoot(self, player, world):
        if self.checkReady(): 
            if player.facingRight:
                pos = [player.rect.right, player.rect.centery]
                world.projectiles.append(Projectile.Bullet(1, pos))
            else:
                pos = [player.rect.left, player.rect.centery]
                world.projectiles.append(Projectile.Bullet(-1, pos))
            self.lastShot = pygame.time.get_ticks()

class RocketLauncher(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.fireDelay = 2000
    def shoot(self, player, world):
        if self.checkReady(): 
            if player.facingRight:
                pos = [player.rect.right, player.rect.centery]
                world.projectiles.append(Projectile.Rocket(1, pos))
            else:
                pos = [player.rect.left, player.rect.centery]
                world.projectiles.append(Projectile.Rocket(-1, pos))
            self.lastShot = pygame.time.get_ticks()
class MachineGun(Weapon):
    #TODO: Random Thingy-thing

    def __init__(self):
        Weapon.__init__(self)
        self.fireDelay = 150
        self.rapidFire = True
    def shoot(self, player, world): 
        if self.checkReady(): 
            if player.facingRight:
                pos = [player.rect.right, player.rect.centery]
                world.projectiles.append(Projectile.Bullet(1, pos))
            else:
                pos = [player.rect.left, player.rect.centery]
                world.projectiles.append(Projectile.Bullet(-1, pos))
            self.lastShot = pygame.time.get_ticks()
            
class DualPistols(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.fireDelay = 100
    def shoot(self, player, world):
        if self.checkReady():
            pos1 = [player.rect.right, player.rect.centery]
            pos2 = [player.rect.left, player.rect.centery]
            world.projectiles.append(Projectile.Bullet(1, pos1))
            world.projectiles.append(Projectile.Bullet(-1, pos2))
            self.lastShot = pygame.time.get_ticks()

class DiskGun(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.fireDelay = 750
    def shoot(self, player, world):
        if self.checkReady():
            if player.facingRight:
                pos = [player.rect.right + 17, player.rect.centery]
                world.projectiles.append(Projectile.Disk(1, pos))
            else:
                pos = [player.rect.left - 17, player.rect.centery]
                world.projectiles.append(Projectile.Disk(-1, pos))
            self.lastShot = pygame.time.get_ticks()
            
class GrenadeLauncher(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.fireDelay = 750
    def shoot(self, player, world):
        if self.checkReady():
            if player.facingRight:
                pos = [player.rect.right, player.rect.centery]
                world.projectiles.append(Projectile.Grenade(1, pos))
            else:
                pos = [player.rect.left, player. rect.centery]
                world.projectiles.append(Projectile.Grenade(-1, pos))
            self.lastShot = pygame.time.get_ticks()
                