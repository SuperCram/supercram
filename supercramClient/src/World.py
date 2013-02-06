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
            tagPlayerSpawns.tags.append(cereal.TagArray([cereal.TagInt(point[0]), cereal.TagInt(point[1])]))
        
        tagMobSpawns = cereal.TagArray()
        for point in self.mobSpawns:
            tagMobSpawns.tags.append(cereal.TagArray([cereal.TagInt(point[0]), cereal.TagInt(point[1])]))
        tagCrateSpawns = cereal.TagArray()
        for zone in self.crateSpawnZones:
            tagCrateSpawns.tags.append(cereal.TagArray([cereal.TagInt(zone.top), cereal.TagInt(zone.left), cereal.TagInt(zone.width), cereal.TagInt(zone.height)]))
        
        worldTag = cereal.TagMap()
        worldTag.data["spirtes"] = sprites
        worldTag.data["playerSpawns"] = tagPlayerSpawns
        worldTag.data["mobSpawns"] = tagMobSpawns
        worldTag.data["crateSpawnPoints"] = tagCrateSpawns
        worldTag.data["gravity"] = cereal.TagFloat(self.gravity)
        worldTag.data["size"] = cereal.TagArray([cereal.TagInt(self.size[0]), cereal.TagInt(self.size[1])])
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
    tagSpriteArray = tagMap["spirtes"].tags
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
    tagPlayerSpawns = tagMap["playerSpawns"].tags
    for tagPlayerSpawn in tagPlayerSpawns:
        world.playerSpawns.append([tagPlayerSpawn.tags[0].i, tagPlayerSpawn.tags[1].i])
    
    tagMobSpawns = tagMap["mobSpawns"].tags
    for tagMobSpawn in tagMobSpawns:
        world.mobSpawns.append([tagMobSpawn.tags[0].i, tagMobSpawn.tags[1].i])
        
    tagMobSpawns = tagMap["mobSpawns"].tags
    for tagMobSpawn in tagMobSpawns:
        world.mobSpawns.append([tagMobSpawn.tags[0].i, tagMobSpawn.tags[1].i])
        
    tagCrateSpawnZones = tagMap["crateSpawnPoints"].tags
    for tagCrateSpawnZone in tagCrateSpawnZones:
        zoneAr = tagCrateSpawnZone.tags
        world.crateSpawnZones.append(pygame.Rect(zoneAr[0].i, zoneAr[1].i, zoneAr[2].i, zoneAr[3].i))
    
    world.gravity = tagMap["gravity"].float
    world.enemySpawnDelay = tagMap["enemySpawnDelay"].i
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





