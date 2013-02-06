<<<<<<< HEAD
=======
from struct import pack,unpack
def readTag(dataStream, read=True):
    tagID = int(dataStream.readByte())
    t = None
    if tagID == 1:
        t = TagByte()
    elif tagID == 2:
        t = TagString()
    elif tagID == 3:
        t = TagInt()
    elif tagID == 4:
        t = TagBool()
    elif tagID == 5:
        t = TagFloat()
    elif tagID == 6:
        t = TagArray([])
    elif tagID == 7:
        t = TagMap({})
    else:
        raise ValueError("Unknown Tag by index "+str(tagID))
    if(read):
        t.read(dataStream)
    return t
class Tag():
    def __init__(self):
        self.id = 0
    def read(self, dataStream):
        pass
    def write(self, dataStream):
        pass

class TagByte(Tag):
    def __init__(self, b=0):
        self.data = b
        self.id = 1
    def read(self, dataStream):
        self.data = dataStream.readByte()
    def write(self,dataStream):
        dataStream.writeByte(self.data)
    def __repr__(self):
        return "TagByte("+str(self.data)+")"
        
class TagString(Tag):
    def __init__(self, s=""):
        self.data = s
        self.id = 2
    def read(self, dataStream):
        self.data = dataStream.readString()
    def write(self, dataStream):
        dataStream.writeString(self.data)
    def __repr__(self):
        return "TagString("+self.data+")"

class TagInt(Tag):
    def __init__(self, i=0):
        self.data = i
        self.id = 3
    def read(self, dataStream):
        self.data = dataStream.readInt()
    def write(self,dataStream):
        dataStream.writeInt(self.data)
    def __repr__(self):
        return "TagInt("+str(self.data)+")"

class TagBool(Tag):
    def __init__(self, b=False):
        self.data = b
        self.id = 4
    def read(self, dataStream):
        self.data = dataStream.readBool()
    def write(self,dataStream):
        dataStream.writeBool(self.data)
    def __repr__(self):
        return "TagBool("+str(self.data)+")"

class TagFloat(Tag):
    def __init__(self, f=0):
        self.data = f
        self.id = 5
    def read(self, dataStream):
        self.data = dataStream.readFloat()
    def write(self,dataStream):
        dataStream.writeFloat(self.data)
    def __repr__(self):
        return "TagFloat("+str(self.data)+")"

class TagArray(Tag):
    def __init__(self, arr=[]):
        self.data = arr
        self.id = 6
    def read(self, dataStream):
        size = dataStream.readInt()
        for i in range(size):
            self.data.append(readTag(dataStream))
    def write(self, dataStream):
        dataStream.writeInt(len(self.data))
        for t in self.data:
            dataStream.writeByte(t.id)
            t.write(dataStream)
    def __repr__(self):
        return "TagArray("+str(self.data)+")"

class TagMap(Tag):
    def __init__(self, map={}):
        self.id = 7
        self.data = map
    def read(self, dataStream):
        tagSize = dataStream.readInt()
        for i in range(tagSize):
            key = dataStream.readString()
            tagToRead = readTag(dataStream)
            self.data[key] = tagToRead
    def write(self, dataStream):
        dataStream.writeInt(len(self.data))
        for t in self.data:
            dataStream.writeString(t)
            dataStream.writeByte(self.data[t].id)
            self.data[t].write(dataStream)
    def __repr__(self):
        return "TagMap("+str(self.data)+")"
class DataInputStream:
    def __init__(self, base_stream):
        self.base_stream = base_stream
    def readByte(self):
        return ord(self.base_stream.read(1))
    def readBytes(self, length):
        return self.base_stream.read(length)
    def readChar(self):
        f = bytearray(self.readBytes(2))
        f.reverse()
        return str(f).decode("UTF-16LE")
    def readBool(self):
        return self.unpack('?')
    def readInt(self):
        return self.unpack('!i', 4)
    def readFloat(self):
        return self.unpack('!f', 4)
    def readString(self):
        length = self.readInt()
        s = ""
        for l in range(length):
            c = self.readChar()
            s += c
        return s
        #return self.unpack(str(length) + 's', length)
    def readTag(self):
        return readTag(self)
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
if(__name__=="__main__"):
    testFile = open("test.db","wb")
    dos = DataOutputStream(testFile)
    dos.writeChar('G');
    dos.writeByte(100);
    dos.writeBool(False)
    dos.writeInt(63324)
    dos.writeFloat(0.5)
    dos.writeString("FOOBAR")
    testFile.close()
    
    testFile = open("test.db","rb")
    dis = DataInputStream(testFile)
    print dis.readChar()
    print dis.readByte()
    print dis.readBool()
    print dis.readInt()
    print dis.readFloat()
    print len(dis.readString())
    testFile.close()
    
    
    g = TagMap({"data":TagArray([TagBool(False), TagInt(12), TagString("APPLE")]), "other":TagArray([TagFloat(0.5), TagByte(124), TagString("sup")])})
    #g = TagArray([TagBool(False), TagInt(12), TagString("APPLE")])
    #g = TagMap({"a":TagString("v")})
    print g
    testFile = open("test.db","wb")
    dos = DataOutputStream(testFile)
    dos.writeByte(g.id)
    g.write(dos)
    testFile.close()
    
    testFile = open("test.db","rb")
    dis = DataInputStream(testFile)
    newTag = readTag(dis)
    testFile.close()
    
    print newTag
    











>>>>>>> branch 'master' of http://github.com/SuperCram/supercram.git
