'''
Player subclass extends Entity
'''
from Entity import Entity
from Weapon import Pistol
import const
from pygame.locals import *

class Player(Entity):
    def __init__(self):
        Entity.__init__(self)
        self.weapon = Pistol()
        self.playerCharacter = 0
        self.onGround = True
        self.facingRight = True
        self.jumping= False
        self.jumpStart = 0
    def checkOnGround(self, collideList):
        for r in collideList:
            for point in [self.rect.bottomleft, self.rect.midbottom, [self.rect.right-1, self.rect.bottom]]:
                if r.rect.collidepoint(point):
                    return True 
        return False

####
    def update(self, world, keysDown):
####

    #Check if on ground
        self.onGround = self.checkOnGround(world.map)
       
    #Get Left/Right keys
        if K_LEFT in keysDown: l = True
        else: l = False
        if K_RIGHT in keysDown: r = True
        else: r = False

    #Jumping
        #If on ground and jump key hit, start jump
        if self.onGround and (K_UP in keysDown or K_z in keysDown):
            self.jumping = True
            self.jumpStart = self.rect.bottom
        if self.jumping:
        #Check if below min jump height
            if self.rect.bottom > (self.jumpStart - const.minJump):
                self.momentum[1] = -const.playerJumpSpeed
        #Check if below max jump height
            elif self.rect.bottom > (self.jumpStart - const.maxJump) and (K_UP in keysDown or K_z in keysDown):
                self.momentum[1] = -const.playerJumpSpeed
            else:
                self.jumping = False      
        
    #Horizontal movement
        if l and r:
            self.momentum[0] = 0
        elif l:
            self.momentum[0] = -const.playerSpeed
        elif r:
            self.momentum[0] = const.playerSpeed
        else:
            self.momentum[0] = 0
            
    #Superclass - updates position, checks collisions
        josh = Entity.update(self, world)
        if self.jumping and josh[1]:
            self.jumping = False

        if world.multiplayer:
            pass   
        else:                
    #Shooting
            if self.weapon.rapidFire == False:
                for e in world.eList:
                    if e.type == KEYDOWN and e.key == K_x:
                        self.weapon.shoot(self, world)
            else:
                if K_x in keysDown:
                    self.weapon.shoot(self, world)

    #Check if collided with any enemies
            for enemy in world.enemies:
                if self.rect.colliderect(enemy.rect):
    ###############################
                    enemy.rect.topleft = (100, 100)
                    self.rect.topleft = (400, 100)
    
    #Check if collided with any playerIntact projectiles
            for proj in world.projectiles:
                if proj.playerInteract and self.rect.colliderect(proj.rect):
    ###############################
                    self.rect.topleft = (400, 100)
    
    #Update facing direction
        if self.momentum[0] > 0:
            self.facingRight = True
        elif self.momentum[0] < 0:
            self.facingRight = False
    
            
            