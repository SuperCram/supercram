'''
Enemy subclass extends Entity
'''

from Entity import Entity
import const

class Enemy(Entity):
    def __init__(self):
        Entity.__init__(self)
        self.type = 0
        self.rage = False
        self.health = 1
        self.dead = False
        self.facingRight = True
    def update(self, world):
        
#Check if colliding with a projectile ie has been hit, and deals damage accordingly
        for proj in world.projectiles:
            if self.rect.colliderect(proj.rect):
                proj.hitEnemy(world)
                self.health -= proj.damage

#Kill if health <= 0
        self.image.fill((255,0,0))
        if self.health <= 0:
##############################
            world.enemies.remove(self)

#Call superclass update, returns true if enemy has hit a wall and reverses direction of travel
        if Entity.update(self, world)[0]:
            self.facingRight = not self.facingRight

#Select speed, dir based on facingRight and rage
        if self.facingRight and not self.rage:
            self.momentum[0] = const.enemySpeed
        elif self.facingRight:
            self.momentum[0] = const.rageSpeed
        elif not self.facingRight and not self.rage:
            self.momentum[0] = -const.enemySpeed
        elif not self.facingRight and self.rage:
            self.momentum[0] = -const.rageSpeed
        else:
            self.momentum[1] = 0
        