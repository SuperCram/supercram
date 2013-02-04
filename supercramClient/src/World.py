'''
World superclass, represents on-screen level and all contents 
'''
        
class World():
    def __init__(self):
        self.map = [] #WorldSprites
        self.playerSpawns = [] #Ints, bottom center
        self.mobSpawns = [] #Ints
        self.mobTriggers = [] #Rects
        self.crateSpawnZones = [] #Rects
        self.players = []
        self.enemies = []
        self.effects = []
        self.crates = []
        self.projectiles = []
        self.drawList = []
        self.eList = []
        self.entList = [self.players, self.enemies, self.effects, self.projectiles, self.crates]
        self.gravity = 600
        self.size = [0,0]
        self.multiplayer = False
        self.enemySpawnDelay = 4000
        self.lastEnemySpawn = 0
    def buildRectLs(self):
        rectLs = []
        for ls in self.entList:
            for e in ls:
                rectLs.append((e.rect.top, e.rect.left, e.rect.width, e.rect.height))
                rectLs.append((e.prevRect.top, e.prevRect.left, e.prevRect.width, e.prevRect.height))
        return rectLs
    def buildDrawList(self):
        self.drawList = [self.map, self.players, self.enemies, self.effects, self.projectiles, self.crates]
    def buildEntList(self):
        self.entList = [self.players, self.enemies, self.effects, self.projectiles, self.crates]
    def draw(self, screen):
        for ls in self.drawList:
            for e in ls:
                screen.blit(e.image, e.rect)

