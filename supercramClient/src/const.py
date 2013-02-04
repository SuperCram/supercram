#Global constants
import math
from Weapon import *

# Movement
playerSpeed = 10
playerJumpSpeed = 15
minJump = 50
maxJump = 100
enemySpeed = 8
rageSpeed = 16

# Weapon List
weapons = [RocketLauncher(), MachineGun(), DualPistols(), DiskGun(), GrenadeLauncher()]

# Colours

white = (255,255,255)

def distance(a, b):
    distX = math.fabs(a[0] - b[0])
    distY = math.fabs(a[1] - b[1])
    return math.hypot(distX, distY)