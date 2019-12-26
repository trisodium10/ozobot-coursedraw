import sys
import matplotlib.pyplot as plt

libpath = "/home/hayman/python/ozobot-coursedraw/libraries"
if not libpath in sys.path:
    sys.path.append(libpath)

import path_utils as pu

save_path = '/home/hayman/python/ozobot-coursedraw/courses/'

BotPath = pu.Ozo_Path((8,5))
BotPath.set_position([0.5,0.5])

BotPath.add_step(pu.black, count=2)

# Pause for 3 seconds
BotPath.add_step_seq([pu.red,pu.blue,pu.red])

BotPath.add_step(pu.black,count=4)

BotPath.set_direction(90)
BotPath.add_step(pu.green,count=12)

BotPath.set_direction(0)
BotPath.add_step(pu.blue,count=8)
BotPath.add_step(pu.black,count=3)

# U-Turn
BotPath.add_step_seq([pu.blue,pu.red])





BotPath.savefig(save_path+'Jenny.png')
BotPath.show()