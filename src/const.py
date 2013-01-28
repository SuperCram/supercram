#Global constants
import math
from Weapon import *

playerSpeed = 10
playerJumpSpeed = 15
minJump = 50
maxJump = 100
enemySpeed = 8
rageSpeed = 16
weapons = [RocketLauncher(), MachineGun(), DualPistols(), DiskGun(), GrenadeLauncher()]

def distance(a, b):
    distX = math.fabs(a[0] - b[0])
    distY = math.fabs(a[1] - b[1])
    return math.hypot(distX, distY)