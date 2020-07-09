import c4d
import math

def main():
    obj = op.GetObject()
    frame = doc.GetTime().GetFrame(doc.GetFps())

    # selected = doc.GetActiveObjects(0)
    objectname = op.GetObject().GetName()
    # print(selected)
    # print(objectname)

    xp = obj[c4d.ID_BASEOBJECT_REL_POSITION, c4d.VECTOR_X]
    yp = obj[c4d.ID_BASEOBJECT_REL_POSITION, c4d.VECTOR_Y]
    zp = obj[c4d.ID_BASEOBJECT_REL_POSITION, c4d.VECTOR_Z]
    xr = obj[c4d.ID_BASEOBJECT_REL_ROTATION, c4d.VECTOR_X] * 180 / math.pi
    yr = obj[c4d.ID_BASEOBJECT_REL_ROTATION, c4d.VECTOR_Y] * 180 / math.pi
    zr = obj[c4d.ID_BASEOBJECT_REL_ROTATION, c4d.VECTOR_Z] * 180 / math.pi

    data = obj[c4d.ID_USERDATA, 1] + "\n" + objectname + "," + str(frame) + "," + str(xp) + "," + str(yp) + "," + str(
        zp) + "," + str(xr) + "," + str(yr) + "," + str(zr)
    
    obj[c4d.ID_USERDATA, 1] = data
