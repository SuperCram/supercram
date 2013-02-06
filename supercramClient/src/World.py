'''
World superclass, represents on-screen level and all contents 
'''
import cereal,WorldSprite,pygame
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
            tagPlayerSpawns.data.append(cereal.TagArray([cereal.TagInt(point[0]), cereal.TagInt(point[1])]))
        
        tagMobSpawns = cereal.TagArray()
        for point in self.mobSpawns:
            tagMobSpawns.data.append(cereal.TagArray([cereal.TagInt(point[0]), cereal.TagInt(point[1])]))
        tagCrateSpawns = cereal.TagArray()
        for zone in self.crateSpawnZones:
            tagCrateSpawns.data.append(cereal.TagArray([cereal.TagInt(zone[0]), cereal.TagInt(zone[1]), cereal.TagInt(zone[2]), cereal.TagInt(zone[3])]))
        
        worldTag = cereal.TagMap()
        worldTag.data["spirtes"] = sprites
        worldTag.data["playerSpawns"] = tagPlayerSpawns
        worldTag.data["mobSpawns"] = tagMobSpawns
        worldTag.data["crateSpawnZones"] = tagCrateSpawns
        worldTag.data["gravity"] = cereal.TagFloat(self.gravity)
        worldTag.data["enemySpawnDelay"] = cereal.TagInt(self.enemySpawnDelay)
        
        return worldTag
    
    def saveWorld(self, name):
        tagMap = self.toTag()
        fileOut = open(name + '.scw', 'wb')
        tagMap.write(fileOut)
        fileOut.close()
        
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
        self.enemySpawnDelay = 4000
        self.lastEnemySpawn = 0
    def __repr__(self):
        s = ""
        s += str(len(self.clips))+"clips "
        s += str(len(self.triggers))+"triggers "
        s += str(len(self.backgrounds))+"backgrounds "
        s += str(len(self.foregrounds))+"foregrounds "
        s += str(len(self.playerSpawns))+"playerSpawns "
        s += str(len(self.mobSpawns))+"mobSpawns "
        s += str(len(self.crateSpawnZones))+"crateSpawnZones "
        s += str(self.enemySpawnDelay)+"enemySpawnDelay "
        s += str(self.gravity)+"gravity "
        return s
    def buildRectLs(self):
        rectLs = []
        for ls in self.entList:
            for e in ls:
                rectLs.append((e.rect.top, e.rect.left, e.rect.width, e.rect.height))
                rectLs.append((e.prevRect.top, e.prevRect.left, e.prevRect.width, e.prevRect.height))
        return rectLs
    def buildDrawList(self):
        self.drawList = [self.backgrounds, self.players, self.enemies, self.effects, self.projectiles, self.crates, self.foregrounds]
    def buildEntList(self):
        self.entList = [self.players, self.enemies, self.effects, self.projectiles, self.crates]
    def draw(self, screen):
        for ls in self.drawList:
            for e in ls:
                screen.blit(e.image, e.rect)
                
def readWorld(tagMap):
    world = World()
    tagMap = tagMap.data
    tagSpriteArray = tagMap["spirtes"].data
    for tagSprite in tagSpriteArray:
        spr = WorldSprite.tagToSprite(tagSprite)
        if(spr.background):
            world.backgrounds.append(spr)
        else:
            world.foregrounds.append(spr)
        if(spr.collisions):
            world.clips.append(spr)
        if(spr.trigger):
            world.triggers.append(spr)
    tagPlayerSpawns = tagMap["playerSpawns"].data
    for tagPlayerSpawn in tagPlayerSpawns:
        world.playerSpawns.append([tagPlayerSpawn.data[0].data, tagPlayerSpawn.data[1].data])
    
    tagMobSpawns = tagMap["mobSpawns"].data
    for tagMobSpawn in tagMobSpawns:
        world.mobSpawns.append([tagMobSpawn.data[0].data, tagMobSpawn.data[1].data])
        
    tagCrateSpawnZones = tagMap["crateSpawnZones"].data
    for tagCrateSpawnZone in tagCrateSpawnZones:
        zoneAr = tagCrateSpawnZone.data
        world.crateSpawnZones.append([zoneAr[0].data, zoneAr[1].data, zoneAr[2].data, zoneAr[3].data])
    
    world.gravity = tagMap["gravity"].data
    world.enemySpawnDelay = tagMap["enemySpawnDelay"].data
    return world
if __name__=="__main__":
    world = World()
    world.clips.append(WorldSprite.WorldSprite(1,2,3,4))
    world.clips[0].background = True
    world.gravity = 10002
    world.enemySpawnDelay = 19292
    print world
    someTag = world.toTag()
    newWorld = readWorld(someTag)
    print newWorld





