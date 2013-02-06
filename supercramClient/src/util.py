import cereal

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
    