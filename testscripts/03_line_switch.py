import sys
import matplotlib.pyplot as plt

libpath = "/home/hayman/python/ozobot-coursedraw/libraries"
if not libpath in sys.path:
    sys.path.append(libpath)

import path_utils as pu

save_path = '/home/hayman/python/ozobot-coursedraw/courses/'

BotPath = pu.Ozo_Path((10,6))

BotPath.set_position([1,6])

BotPath.add_step(pu.black,count=5)

# lineswitch left
BotPath.add_step_seq([pu.green,pu.red,pu.green])
BotPath.store_position(label='lineswitch left 1')

BotPath.add_step(pu.black,count=39)
BotPath.add_turn(180,rate=0.2,step_number=40)
BotPath.add_step(pu.black,count=15)
BotPath.add_step_seq([pu.blue,pu.red])

BotPath.shift_position(-10,0)
BotPath.add_step_seq([pu.red,pu.blue])
BotPath.add_step(pu.black,count=12)

BotPath.add_turn(-45,rate=0.1,step_number=10)
BotPath.add_step(pu.black,count=6)

BotPath.add_turn(-90,rate=0.1,step_number=20)
BotPath.add_step(pu.black,count=6)

BotPath.add_step_seq([pu.red,pu.green,pu.red])
BotPath.store_position(label='lineswitch right 2')
BotPath.add_step(pu.black,count=4)

BotPath.add_step_seq([pu.blue,pu.red,])

BotPath.shift_position(4.5,-1.0)
BotPath.set_rel_direction(180)
BotPath.add_step_seq([pu.red,pu.blue,])
BotPath.add_step(pu.black,count=12)


BotPath.add_turn(90,rate=0.1,step_number=20)
BotPath.add_turn(45,rate=0.1,step_number=10)
BotPath.add_step(pu.black)
BotPath.add_step_seq([pu.red,pu.green,pu.black,pu.blue])
BotPath.add_step(pu.black,count=20)

BotPath.add_step_seq([pu.red,pu.green,pu.red])
BotPath.store_position(label='lineswitch right 3')
BotPath.add_step(pu.black,count=8)

# Bottom Path
BotPath.set_position([0,1])
BotPath.set_direction(0)
BotPath.add_step_seq([pu.red,pu.blue,])
BotPath.add_step(pu.black,count=8)

# Tornado
BotPath.add_step_seq([pu.red,pu.green,]*2)

BotPath.add_step(pu.black,count=20)

# End
BotPath.add_step_seq([pu.green,pu.red])


BotPath.savefig(save_path+'LineSwitch.png')
BotPath.show()