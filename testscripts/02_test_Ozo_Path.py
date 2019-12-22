

import sys
import matplotlib.pyplot as plt

libpath = "/home/hayman/python/ozobot/libraries"
if not libpath in sys.path:
    sys.path.append(libpath)

save_path = '/home/hayman/python/ozobot/courses/'

import path_utils as pu

BotPath = pu.Ozo_Path((8,5))

BotPath.set_position([1,1.0])
BotPath.add_step(pu.black,count=6)
BotPath.add_fast()
BotPath.add_step(pu.black,count=3)

# Tornado
BotPath.add_step(pu.red)
BotPath.add_step(pu.green)
BotPath.add_step(pu.red)
BotPath.add_step(pu.green)
BotPath.add_step(pu.black,count=5)

# Turn Up
counter = 0
while counter < 9:
    BotPath.set_rel_direction(10)
    BotPath.add_step(pu.black)
    counter+=1

BotPath.add_step(pu.green,count=6)

# Turn Up
counter = 0
while counter < 9:
    BotPath.set_rel_direction(10)
    BotPath.add_step(pu.black)
    counter+=1

BotPath.add_step(pu.blue,count=12)
BotPath.add_step(pu.black,count=4)

# Turbo
BotPath.add_step(pu.blue)
BotPath.add_step(pu.green)
BotPath.add_step(pu.blue)

BotPath.add_step(pu.black,count=2)

# Turn Up
counter = 0
while counter < 9:
    BotPath.set_rel_direction(10)
    BotPath.add_step(pu.red)
    counter+=1
    
BotPath.add_step(pu.black,count=6)

# Turn Up
counter = 0
while counter < 9:
    BotPath.set_rel_direction(10)
    BotPath.add_step(pu.blue)
    counter+=1

BotPath.savefig(save_path+'TestFile.png')

BotPath.show()

