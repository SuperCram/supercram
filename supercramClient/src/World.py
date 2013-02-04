'''
World superclass, represents on-screen level and all contents 
'''
import cereal   
class World():
    def toTag(self):
        sprites = []
        
        for worldSprite in self.clips:
            sprites.append(worldSprite.toTag())
        for worldSprite in self.triggers:
            sprites.append(worldSprite.toTag())
        for worldSprite in self.backgrounds:
            sprites.append(worldSprite.toTag())
        for worldSprite in self.foregrounds:
            sprites.append(worldSprite.toTag())
        sprites = cereal.TagArray(sprites)
        
        #Player Spawns
        tagPlayerSpawns = cereal.TagArray()
        for point in self.playerSpawns:
            tagPlayerSpawns.tags.append(cereal.TagArray([cereal.TagInt(point[0]), cereal.TagInt(point[1])]))
        
        tagMobSpawns = cereal.TagArray()
        for point in self.mobSpawns:
            tagMobSpawns.tags.append(cereal.TagArray([cereal.TagInt(point[0]), cereal.TagInt(point[1])]))
        tagCrateSpawns = cereal.TagArray()
        for zone in self.crateSpawnZones:
            tagCrateSpawns.tags.append(cereal.TagArray([cereal.TagInt(zone.left), cereal.TagInt(zone.top), cereal.TagInt(zone.width), cereal.TagInt(zone.height)]))
        
        worldTag = cereal.TagMap()
        worldTag.data["spirtes"] = sprites
        worldTag.data["playerSpawns"] = tagPlayerSpawns
        worldTag.data["mobSpawns"] = tagMobSpawns
        worldTag.data["crateSpawnPoints"] = tagCrateSpawns
        worldTag.data["gravity"] = cereal.TagFloat(self.gravity)
        worldTag.data["size"] = cereal.TagArray([cereal.TagInt(self.size[0]), cereal.TagInt(self.size[1])])
        worldTag.data["enemySpawnDelay"] = cereal.TagInt(self.enemySpawnDelay)
        
        return worldTag
        
    def __init__(self):
        self.clips = []
        self.triggers = []
        self.backgrounds = []
        self.foregrounds = []
        
        self.playerSpawns = [] #Ints, bottom center
        self.mobSpawns = [] #Ints
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

