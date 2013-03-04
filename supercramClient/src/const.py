#Global constants
import math, pygame
from Weapon import *

# Movement
playerSpeed = 10
playerJumpSpeed = 15
minJump = 50
maxJump = 100
enemySpeed = 8
rageSpeed = 16

#Colours
white = (255,255,255)
red = (255,0,0)

# Weapon List
weapons = [RocketLauncher(), MachineGun(), DualPistols(), DiskGun(), GrenadeLauncher()]

#Enemy Params
enemy0Surf = pygame.Surface((32,32))
enemy0Surf.fill(red)
enemyParams = [(0, 5, (32,32), enemy0Surf)]


def distance(a, b):
    distX = math.fabs(a[0] - b[0])
    distY = math.fabs(a[1] - b[1])
    return math.hypot(distX, distY)