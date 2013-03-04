import cereal
import pygame

def toFile(name, tagmap):
    fileOut = open(name+'.scw', 'wb')
    dos = cereal.DataOutputStream(fileOut)
    dos.writeByte(tagmap.id)
    tagmap.write(dos)
    fileOut.close()
    
def fromFile(name):
    fileIn = open(name+'.scw', 'rb')
    dis = cereal.DataInputStream(fileIn)
    worldtag = cereal.readTag(dis)
    fileIn.close()
    return worldtag
    
if __name__ == '__main__':
    
    surf = pygame.Surface((800,600))
    surf.fill((0,0,0))
    pygame.draw.polygon(surf, (255,0,0), [(20, 50), (304, 530), (700, 004)])
    pygame.image.save(surf, 'dummy.bmp')