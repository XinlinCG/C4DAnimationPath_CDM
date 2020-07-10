# xp = obj[c4d.ID_BASEOBJECT_REL_POSITION, c4d.VECTOR_X]
# yp = obj[c4d.ID_BASEOBJECT_REL_POSITION, c4d.VECTOR_Y]
# zp = obj[c4d.ID_BASEOBJECT_REL_POSITION, c4d.VECTOR_Z]
# xr = obj[c4d.ID_BASEOBJECT_REL_ROTATION, c4d.VECTOR_X] * 180 / math.pi
# yr = obj[c4d.ID_BASEOBJECT_REL_ROTATION, c4d.VECTOR_Y] * 180 / math.pi
# zr = obj[c4d.ID_BASEOBJECT_REL_ROTATION, c4d.VECTOR_Z] * 180 / math.pi

# Shoulder_02_XN
# Bicep_03_YN
# Forearm_04_ZN
# TuningFork_05_UN
# PicassoBox_06_VN
# Hand_07_WN

file = open("RawData.txt", "r")
sentences = []
frames = []
key_sequence_of_each_joint = []

key = []

for line in file:
    splitLine = line.split(",")
    sentences.append(line.strip())

file.close()

def getUniqueItems(iterable):
    seen = set()
    result = []
    for item in iterable:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

sentences = getUniqueItems(sentences)

organized = []

for line in sentences:
    splitLine = line.split(",")
    # print(splitLine)

    splitLine[1] = int(splitLine[1])

    splitLine[2] = float(splitLine[2])
    splitLine[3] = float(splitLine[3])
    splitLine[4] = float(splitLine[4])
    splitLine[5] = float(splitLine[5])
    splitLine[6] = float(splitLine[6])
    splitLine[7] = float(splitLine[7])

    organized.append(splitLine)

Shoulder_02_XN = []
Bicep_03_YN = []
Forearm_04_ZN = []
TuningFork_05_UN = []
PicassoBox_06_VN = []
Hand_07_WN = []

for list in organized:
    if list[0] == 'Shoulder_02_XN':
        Shoulder_02_XN.append(list)
    elif list[0] == 'Bicep_03_YN':
        Bicep_03_YN.append(list)
    elif list[0] == 'Forearm_04_ZN':
        Forearm_04_ZN.append(list)
    elif list[0] == 'TuningFork_05_UN':
        TuningFork_05_UN.append(list)
    elif list[0] == 'PicassoBox_06_VN':
        PicassoBox_06_VN.append(list)
    elif list[0] == 'Hand_07_WN':
        Hand_07_WN.append(list)
    else:
        print("This file either contains unexpected object(joints), or the joints' names are named incorrectly")

alljoints = []

alljoints.append(Shoulder_02_XN)
alljoints.append(Bicep_03_YN)
alljoints.append(Forearm_04_ZN)
alljoints.append(TuningFork_05_UN)
alljoints.append(PicassoBox_06_VN)
alljoints.append(Hand_07_WN)

for joint in alljoints:
    xp = []
    yp = []
    zp = []
    xr = []
    yr = []
    zr = []

    for i in joint:
        xp.append(i[2])
        yp.append(i[3])
        zp.append(i[4])
        xr.append(i[5])
        yr.append(i[6])
        zr.append(i[7])

    allaxes = []

    allaxes.append(xp)
    allaxes.append(yp)
    allaxes.append(zp)
    allaxes.append(xr)
    allaxes.append(yr)
    allaxes.append(zr)

    for c in allaxes:
        if len(getUniqueItems(c)) <= 1:
            c = []
        if len(getUniqueItems(c)) > 1:
            joint = c
    key_sequence_of_each_joint.append(joint)



    print(key_sequence_of_each_joint)
    print(" ")
    print(len(key_sequence_of_each_joint))

for i in key_sequence_of_each_joint:
    print(i)
    print(" ")

for i in organized:
    frames.append(i[1])
    frames = getUniqueItems(frames)

for i in frames:
    print( str(i) + "," + "{" +
           "\"xn\":" + str(key_sequence_of_each_joint[0][i]) + "," +
           "\"yn\":" + str(key_sequence_of_each_joint[1][i]) + "," +
           "\"zn\":" + str(key_sequence_of_each_joint[2][i]) + "," +
           "\"un\":" + str(key_sequence_of_each_joint[3][i]) + "," +
           "\"vn\":" + str(key_sequence_of_each_joint[4][i]) + "," +
           "\"wn\":" + str(key_sequence_of_each_joint[5][i]) + "}"
           )
