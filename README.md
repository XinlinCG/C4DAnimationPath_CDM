# Batch Commands Preparation For `Robot Overlord 2`
Sixi is a robotic arm built and developed by [Marginaly Clever](https://www.marginallyclever.com/products/sixi-robot-arm/)

This document explains the steps of the preparation of the batch commands for Sixi's actual movements.

This repository is a subproject of the main project.

The interpreter is Python 3.8

We, a team from [the Centre for Digital Media](https://thecdm.ca/) who are responsible for making an iteration for the current controlling App of Sixi.

### The manipulation of animation path contains 2 stages

1. Data collection from animated joints in C4D or other softwares
2. Data manipulation in order to export the batch-ready commands

## 1st Stage:

Data colletion is done by the code named `C4dExtraction.py`
It records all the position and rotation coordinates.(Positions of x,y,z, Rotations of x,y,z) of each animated frame of each joint

Caution: Only one coordinate is supposed to have variational data, other coordinates should have the same number.(One joint can only move along one axis)

If the animation glitches appear:
Temporary Solution: Zero out the unused joints in `C4dExtraction.py` of each joint

The joints' names are

    # Shoulder_02_X
        # Bicep_03_Y
            # Forearm_04_Z
                # TuningFork_05_U
                    # PicassoBox_06_V
                        # Hand_07_W
                            # Clamps_08_T

The lower ones are the highers ones' children
    
 After collecting the data of each joint, we paste them into a txt file. (e.g. `raw_anim_01.txt` is an example)

## 2nd Stage:
Follow the steps of second stage, and you will get a JSON output.

Steps:
1. Open `C4DDataManipulation.py`  in the root directory
2. Load the .txt file (e.g. `raw_anim_01.txt` ) you generated from Stage 1 in Python by replacing the variable `rawDataFile` 
3. Preset the output file by replacing the variable `exportedDataFile`
4. Run `C4DDataManipulation.py`
5. The JSON data will be ready in the output file as you indicated in step 3 

Once the new outfile is generated, it can be distributed and read by Robot Overlord 2.

### Contributor
Xinlin (Bigger) Yang @ the Centre for Digital Media

