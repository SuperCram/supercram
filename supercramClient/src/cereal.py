class Tag():
    
    def __init__(self):
        self.id = 0
    def read(self, dataStream):
        pass
    def write(self, dataStream):
        pass
    def readTag(self, dataStream):
        tagID = dataStream.readByte()
        if tagID == 1:
            return TagByte()
        if tagID == 2:
            return TagString()
        elif tagID == 3:
            return TagInt()
        elif tagID == 4:
            return TagBool()
        elif tagID == 5:
            return TagFloat()
        elif tagID == 6:
            return TagArray()
        elif tagID == 7:
            return TagMap()
        else:
            raise ValueError

class TagByte(Tag):
    def __init__(self, b):
        self.byte = b
        self.id = 1
    def read(self, dataStream):
        self.byte = dataStream.readByte()
    def write(self,dataStream):
        dataStream.writeByte(self.byte)
        
class TagString(Tag):
    def __init__(self, s):
        self.string = s
        self.id = 2
    def read(self, dataStream):
        self.string = dataStream.readString()
    def write(self, dataStream):
        dataStream.writeString()

class TagInt(Tag):
    def __init(self, i):
        self.i = i
        self.id = 3
    def read(self, dataStream):
        self.i = dataStream.readInt()
    def write(self,dataStream):
        dataStream.writeInt(self.i)

class TagBool(Tag):
    def __init__(self, b):
        self.bool = b
        self.id = 4
    def read(self, dataStream):
        self.bool = dataStream.readBool()
    def write(self,dataStream):
        dataStream.writeBool(self.bool)

class TagFloat(Tag):
    def __init__(self, f):
        self.float = f
        self.id = 5
    def read(self, dataStream):
        self.float = dataStream.readFloat()
    def write(self,dataStream):
        dataStream.writeFloat(self.float)

class TagArray(Tag):
    def __init__(self):
        self.tags = []
        self.id = 6
    def read(self, dataStream):
        size = dataStream.readInt()
        for i in range(size):
            newTag = Tag.readTag(dataStream)
            newTag.read(dataStream)
            self.tags.append(newTag)
    def write(self, dataStream):
        dataStream.writeInt(len(self.tags))
        for t in self.tags:
            dataStream.writeByte(t.id)
            t.write(dataStream)

class TagMap(Tag):
    def _init__(self):
        self.id = 7
        self.data = {}
    def read(self, dataStream):
        tagSize = dataStream.readInt()
        for i in range(tagSize):
            key = dataStream.readString()
            tag = Tag.readTag(dataStream)
            tag.read(dataStream)
            self.data[key] = tag
    def write(self, dataStream):
        dataStream.writeInt(len(self.data))
        for t in self.data:
            dataStream.writeString(t)
            dataStream.writeByte(self.data[t].id)
            self.data[t].write(dataStream)
