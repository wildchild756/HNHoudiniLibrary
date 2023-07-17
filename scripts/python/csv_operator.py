import csv
import struct
import hou

##Load
def GetDefault(value):
    default = "default"
    if isinstance(value,float):
        default = 0.0
    elif isinstance(value,int):
        default = 0
    return default

def LoadCsv(path):
    node = hou.pwd()
    geo = node.geometry()
    isHeader = True
    isFirstRow = True
    header = []
    length = 0
    with open(path)as f:
        data = csv.reader(f)
        for row in data:
            if isHeader:
                length = len(row)
                for i in range(length):
                    header.append(row[i])
                isHeader = False                  
            elif isFirstRow:        
                pnt = geo.createPoint()
                for i in range(length):
                    default = GetDefault(row[i])
                    geo.addAttrib(hou.attribType.Point,header[i], default, False, False)
                    pnt.setAttribValue(header[i],row[i])
                isFirstRow = False
            else:
                pnt = geo.createPoint()
                for i in range(length):                
                    pnt.setAttribValue(header[i],row[i])


##Export
def ExportCsv(path, attrList):
    node = hou.pwd()
    geo = node.geometry()
    f = open(path, "w")
    separator = "," 
    for attr in attrList:
        attrib = geo.findPointAttrib(attr)
        attrCount = attrib.size()
        if 1 != attrCount:
            for i in range(0,attrCount):
                if i > 2:
                    f.write(attrib.name() + " [" + chr(94 + i) + "]" + separator)
                else:
                    f.write(attrib.name() + " [" + chr(88 + i) + "]" + separator)                
        else:
            f.write(attrib.name())
            f.write(separator)           
        
    f.write("\n")        
    for point in geo.points():
        for attr in attrList:
            attrib = geo.findPointAttrib(attr)
            attrCount = attrib.size()
            if 1 != attrCount:
                for i in range(0,attrCount):
                    f.write(str(point.attribValue(attrib)[i]) + separator)
            else:
                f.write(str(point.attribValue(attrib)))
                f.write(separator)
        f.write("\n")
    f.close()
    
