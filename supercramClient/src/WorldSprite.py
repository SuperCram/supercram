'''
WorldSprite superclass, represents world collision boxes, trigger zones
'''
import pygame,cereal

class WorldSprite():
    def __init__(self, left, top, width, height):
        self.collisions = True
        self.background = True
        self.image = ''
        self.type = 0
        self.rect = pygame.Rect(left, top, width, height)
        self.params = {}
    def toTag(self):
        sprite = cereal.TagMap()
        sprite["aabb"] = cereal.TagArray([cereal.TagInt(self.rect.left), cereal.TagInt(self.rect.top), cereal.TagInt(self.rect.width), cereal.TagInt(self.rect.height)])
        sprite["collisions"] = cereal.TagBool(self.collisions)
        sprite["background"] = cereal.TagBool(self.background)
        tagParams = {}
        for param in self.params:
            tagParams[param] = cereal.TagString(self.params[param])
        sprite["params"] = cereal.TagMap(tagParams)
        return sprite
        
