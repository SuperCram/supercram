'''
WorldSprite superclass, represents world collision boxes, trigger zones
'''
import pygame,cereal


class WorldSprite():
    def __init__(self, left, top, width, height):
        self.collisions = True
        self.background = True
        self.trigger = False
        self.image = pygame.Surface((width, height))
        self.rect = pygame.Rect(left, top, width, height)
        self.params = {}
    def toTag(self):
        sprite = {}
        c = [cereal.TagInt(self.rect.left), cereal.TagInt(self.rect.top), cereal.TagInt(self.rect.width), cereal.TagInt(self.rect.height)]
        gj = cereal.TagArray(c)
        sprite["aabb"] = gj
        sprite["collisions"] = cereal.TagBool(self.collisions)
        sprite["background"] = cereal.TagBool(self.background)
        sprite["trigger"] = cereal.TagBool(self.trigger)
        sprite['image'] = cereal.TagString(pygame.image.tostring(self.image, 'RGBA'))
        tagParams = {}
        for param in self.params:
            tagParams[param] = cereal.TagString(self.params[param])
        sprite["params"] = cereal.TagMap(tagParams)
        sprite = cereal.TagMap(sprite)
        return sprite
    def __repr__(self):
        s = ""
        if(self.collisions): s += "collisions "
        if(self.background): s += "background "
        s += "rect="+str(self.rect)
        s += "params="+str(self.params)
        return s
def tagToSprite(TAGMap):
    spriteDict = TAGMap.data
    spr = WorldSprite(0,0,0,0)
    rect = spriteDict["aabb"].data
    spr.rect = pygame.Rect(rect[0].data, rect[1].data, rect[2].data, rect[3].data)
    spr.collisions = spriteDict["collisions"].data
    spr.background = spriteDict["background"].data
    spr.trigger = spriteDict["trigger"].data
    paramMap = spriteDict["params"].data
    spr.image = pygame.image.fromstring(spriteDict['image'].data, (spr.rect.width, spr.rect.height), 'RGBA') 
    spr.params = {}
    for key in paramMap:
        spr.params[key] = paramMap[key].data
    return spr
