import c4d
import math

#Shoulder_02_XN

def main():
    obj = op.GetObject()
    frame = doc.GetTime().GetFrame(doc.GetFps())
    xp = obj[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_Z] * 180 / math.pi
    data = obj[c4d.ID_USERDATA,1]+"\n"+ "Shoulder_02_XN" + "Frame"+str(frame) + "/" + "B_Z_rotation:"+str(xp)
    obj[c4d.ID_USERDATA,1] = data

#Bicep_03_YN

def main():
    obj = op.GetObject()
    frame = doc.GetTime().GetFrame(doc.GetFps())
    xp = obj[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_Y] * 180 / math.pi
    data = obj[c4d.ID_USERDATA,1]+"\n"+ "Bicep_03_YN" + "Frame"+str(frame) + "/" + "P_Y_rotation:"+str(xp)
    obj[c4d.ID_USERDATA,1] = data

#Forearm_04_ZN

def main():
    obj = op.GetObject()
    frame = doc.GetTime().GetFrame(doc.GetFps())
    xp = obj[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_Y] * 180 / math.pi
    data = obj[c4d.ID_USERDATA,1]+"\n"+ "Forearm_04_ZN" + "Frame"+str(frame) + "/" + "P_Y_rotation:"+str(xp)
    obj[c4d.ID_USERDATA,1] = data

#TuningFork_05_UN

def main():
    obj = op.GetObject()
    frame = doc.GetTime().GetFrame(doc.GetFps())
    xp = obj[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_Y] * 180 / math.pi
    data = obj[c4d.ID_USERDATA,1]+"\n"+ "TuningFork_05_UN" + "Frame"+str(frame) + "/" + "P_Y_rotation:"+str(xp)
    obj[c4d.ID_USERDATA,1] = data

#PicassoBox_06_VN

def main():
    obj = op.GetObject()
    frame = doc.GetTime().GetFrame(doc.GetFps())
    xp = obj[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_X] * 180 / math.pi
    data = obj[c4d.ID_USERDATA,1]+"\n"+ "PicassoBox_06_VN" +"Frame"+str(frame) + "/" + "H_X_rotation:"+str(xp)
    obj[c4d.ID_USERDATA,1] = data

#Hand_07_WN

def main():
    obj = op.GetObject()
    frame = doc.GetTime().GetFrame(doc.GetFps())
    xp = obj[c4d.ID_BASEOBJECT_REL_ROTATION,c4d.VECTOR_X] * 180 / math.pi
    data = obj[c4d.ID_USERDATA,1]+"\n"+ "Hand_07_WN" +"Frame"+str(frame) + "/" + "H_X_rotation:"+str(xp)
    obj[c4d.ID_USERDATA,1] = data
