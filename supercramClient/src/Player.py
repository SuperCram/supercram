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
        self.keysDown = []
    def checkOnGround(self, collideList):
        for r in collideList:
            for point in [self.rect.bottomleft, self.rect.midbottom, [self.rect.right-1, self.rect.bottom]]:
                if r.rect.collidepoint(point):
                    return True 
        return False

####
    def update(self, session):
####
    
        for e in session.worlds[session.activeWorld].eList:
            if e.type == KEYDOWN:
                if e.key not in self.keysDown:
                    self.keysDown.append(e.key)
            elif e.type == KEYUP:
                if e.key in self.keysDown:
                    self.keysDown.remove(e.key)

    #Check if on ground
        self.onGround = self.checkOnGround(session.worlds[session.activeWorld].clips)
       
    #Get Left/Right keys
        if K_LEFT in self.keysDown: l = True
        else: l = False
        if K_RIGHT in self.keysDown: r = True
        else: r = False

    #Jumping
        #If on ground and jump key hit, start jump
        if self.onGround and (K_UP in self.keysDown or K_z in self.keysDown):
            self.jumping = True
            self.jumpStart = self.rect.bottom
        if self.jumping:
        #Check if below min jump height
            if self.rect.bottom >= (self.jumpStart - (const.minJump)):
                self.momentum[1] = -const.playerJumpSpeed
        #Check if below max jump height
            elif self.rect.bottom > (self.jumpStart - const.maxJump) and (K_UP in self.keysDown or K_z in self.keysDown):
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
        collisions = Entity.update(self, session.worlds[session.activeWorld])
        if self.jumping and collisions[1]:
            self.jumping = False

        if session.multiplayer:
            pass   
        else:                
    #Shooting
            if self.weapon.rapidFire == False:
                for e in session.worlds[session.activeWorld].eList:
                    if e.type == KEYDOWN and e.key == K_x:
                        self.weapon.shoot(self, session.worlds[session.activeWorld])
            else:
                if K_x in self.keysDown:
                    self.weapon.shoot(self, session.worlds[session.activeWorld])

    #Check if collided with any enemies
            for enemy in session.worlds[session.activeWorld].enemies:
                if self.rect.colliderect(enemy.rect):
    ###############################
                    self.rect.topleft = (400, 100)
                    self.momentum = [0,0]
    
    #Check if collided with any playerIntact projectiles
            for proj in session.worlds[session.activeWorld].projectiles:
                if proj.playerInteract and self.rect.colliderect(proj.rect):
    ###############################
                    self.rect.topleft = (400, 100)
                    self.momentum = [0,0]
    
    #Update facing direction
        if self.momentum[0] > 0:
            self.facingRight = True
        elif self.momentum[0] < 0:
            self.facingRight = False
    
            
            