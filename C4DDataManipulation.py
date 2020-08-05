# xp = obj[c4d.ID_BASEOBJECT_REL_POSITION, c4d.VECTOR_X]
# yp = obj[c4d.ID_BASEOBJECT_REL_POSITION, c4d.VECTOR_Y]
# zp = obj[c4d.ID_BASEOBJECT_REL_POSITION, c4d.VECTOR_Z]
# xr = obj[c4d.ID_BASEOBJECT_REL_ROTATION, c4d.VECTOR_X] * 180 / math.pi
# yr = obj[c4d.ID_BASEOBJECT_REL_ROTATION, c4d.VECTOR_Y] * 180 / math.pi
# zr = obj[c4d.ID_BASEOBJECT_REL_ROTATION, c4d.VECTOR_Z] * 180 / math.pi

# The followings are the current joints attached to Sixi
# The joints in C4D should also be renamed to the exact same names
# Shoulder_02_X
# Bicep_03_Y
# Forearm_04_Z
# TuningFork_05_U
# PicassoBox_06_V
# Hand_07_W
# Clamps_08_T


import numpy as np

rawDataFile = "raw_anim_01.txt"  # Replace the string with the name of the exported file which contains data from c4d
exportedDataFile = "exported_anim_01.txt" # Exported data will be stored in this file

file = open(rawDataFile, "r")
sentences = []
frames = []
key_sequence_of_each_joint = []

key = []

for line in file:
    splitLine = line.split(",")
    sentences.append(line.strip())
    # print(line)

file.close()


# This function deletes repetitive elements in a list. e.g. Coordinates of the joint in the same frame
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

# This loop makes each sentence break down into smaller elements, and convert them into: int, float, string
for line in sentences:
    splitLine = line.split(",")
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
Clamps_08_TN = []

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
    elif list[0] == 'Clamps_08_TN':
        Clamps_08_TN.append(list)
    else:
        print("This file either contains unexpected object(joints), or the joints' names are named incorrectly")

alljoints = []

alljoints.append(Shoulder_02_XN)
alljoints.append(Bicep_03_YN)
alljoints.append(Forearm_04_ZN)
alljoints.append(TuningFork_05_UN)
alljoints.append(PicassoBox_06_VN)
alljoints.append(Hand_07_WN)
alljoints.append(Clamps_08_TN)

# alljoints = [[Joint1[0:-1]][joint2[0:-1]]...[joint8[0:-1]]]
# print(alljoints)

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

    allaxes = [xp, yp, zp, xr, yr, zr]
    # print(allaxes)

    for c in allaxes:

        if len(getUniqueItems(c)) > 1:
            joint = c
            # print(joint)
            break

        if len(getUniqueItems(c)) == 1:
            joint = c

    key_sequence_of_each_joint.append(joint)

#print(key_sequence_of_each_joint)
# print(" ")
#print(len(key_sequence_of_each_joint))
# This loop deletes fixed coordinates(Positions and rotations) of each joint, and assign the key animation path to →
# key_sequence_of_each_joint

# for i in key_sequence_of_each_joint:
# print(i)
# print(" ")

for i in organized:
    frames.append(i[1])
    frames = getUniqueItems(frames)

# print(key_sequence_of_each_joint[6][0])

exportedcommands = open(exportedDataFile, 'w+')
exportedcommands.truncate(0)

exportedcommands.write('[' + '\n')

for i in frames:
    print(str(i) + "," + "{" +
          "\"x\":" + str(round(key_sequence_of_each_joint[0][i], 3)) + "," +
          "\"y\":" + str(round(key_sequence_of_each_joint[1][i] - 90.0, 3)) + "," +
          "\"z\":" + str(round(key_sequence_of_each_joint[2][i], 3)) + "," +
          "\"u\":" + str(round(key_sequence_of_each_joint[3][i], 3)) + "," +
          "\"v\":" + str(round(key_sequence_of_each_joint[4][i], 3)) + "," +
          "\"w\":" + str(round(key_sequence_of_each_joint[5][i], 3)) + "," +
          "\"t\":" + str(round(key_sequence_of_each_joint[6][i], 3)) +
          "}"
          )
    if i == len(frames) - 1:
        exportedcommands.write("{" +
                               "\"x\":" + str(round(key_sequence_of_each_joint[0][i], 3)) + "," +
                               "\"y\":" + str(round(key_sequence_of_each_joint[1][i] - 90.0, 3)) + "," +
                               "\"z\":" + str(round(key_sequence_of_each_joint[2][i], 3)) + "," +
                               "\"u\":" + str(round(key_sequence_of_each_joint[3][i], 3)) + "," +
                               "\"v\":" + str(round(key_sequence_of_each_joint[4][i], 3)) + "," +
                               "\"w\":" + str(round(key_sequence_of_each_joint[5][i], 3)) + "," +
                               "\"t\":" + str(round(key_sequence_of_each_joint[6][i], 3)) +
                               "}" + '\n')
    else:
        exportedcommands.write("{" +
                               "\"x\":" + str(round(key_sequence_of_each_joint[0][i], 3)) + "," +
                               "\"y\":" + str(round(key_sequence_of_each_joint[1][i] - 90.0, 3)) + "," +
                               "\"z\":" + str(round(key_sequence_of_each_joint[2][i], 3)) + "," +
                               "\"u\":" + str(round(key_sequence_of_each_joint[3][i], 3)) + "," +
                               "\"v\":" + str(round(key_sequence_of_each_joint[4][i], 3)) + "," +
                               "\"w\":" + str(round(key_sequence_of_each_joint[5][i], 3)) + "," +
                               "\"t\":" + str(round(key_sequence_of_each_joint[6][i], 3)) +
                               "}" + ',' + '\n')

exportedcommands.write(']')
exportedcommands.close()
