from struct import pack,unpack
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
class DataInputStream:
    def __init__(self, base_stream):
        self.base_stream = base_stream
    def readByte(self):
        return self.base_stream.read(1)
    def readBytes(self, length):
        return self.base_stream.read(length)
    def readChar(self):
        return self.unpack('b')
    def readBool(self):
        return self.unpack('?')
    def readInt(self):
        return self.unpack('i', 4)
    def readFloat(self):
        return self.unpack('f', 4)
    def readString(self):
        length = self.readInt32()
        return self.unpack(str(length) + 's', length)
    def readTag(self):
        return None
    def unpack(self, fmt, length = 1):
        return unpack(fmt, self.readBytes(length))[0]
class DataOutputStream:
    def __init__(self, base_stream):
        self.base_stream = base_stream
    def writeBytes(self, value):
        self.base_stream.write(value)
    def writeChar(self, value):
        ba = bytearray(value.encode('UTF-16LE'))
        ba.reverse()
        self.writeBytes(ba)
    def writeByte(self, value):
        value = value&255
        self.base_stream.write(chr(value))
    def writeBool(self, value):
        self.pack('?', value)
    def writeInt(self, value):
        self.pack('!i', value)
    def writeFloat(self, value):
        self.pack('!f', value)
    def writeString(self, value):
        length = len(value)
        self.writeInt(length)
        for l in range(length):
            self.writeChar(value[l])
    def pack(self, fmt, data):
        return self.writeBytes(pack(fmt, data))