# import matplotlib
# matplotlib.use('Agg')


import sys
import matplotlib.pyplot as plt

libpath = "/home/hayman/python/ozobot-coursedraw/libraries"
if not libpath in sys.path:
    sys.path.append(libpath)

save_path = '/home/hayman/python/ozobot-coursedraw/courses/'

import path_utils as pu

BotPath = pu.Ozo_Path((8,5))

BotPath.set_position([1.5,0.5])
BotPath.add_step(pu.black,count=6)
BotPath.add_fast()
BotPath.add_step(pu.black,count=3)

# Tornado
BotPath.add_step_seq([pu.red,pu.green,]*2)
# BotPath.add_step(pu.red)
# BotPath.add_step(pu.green)
# BotPath.add_step(pu.red)
# BotPath.add_step(pu.green)
BotPath.add_step(pu.black,count=5)

# Turn Up
BotPath.add_turn(90,rate=0.5,step_number=20)
# counter = 0
# while counter < 18:
#     BotPath.set_rel_direction(5)
#     BotPath.add_step(pu.black,step_frac=0.5)
#     counter+=1

BotPath.add_step(pu.green,count=6)

# Turn Up
BotPath.add_turn(90,rate=0.5,step_number=20)

BotPath.add_step(pu.blue,count=12)
BotPath.add_step(pu.black,count=4)

# Turbo
BotPath.add_step_seq([pu.blue,pu.green,pu.blue])

BotPath.add_step(pu.black,count=2)

# Turn Up
BotPath.add_turn(90,rate=0.5,step_number=20,color=pu.red)
    
BotPath.add_step(pu.black,count=6)

# Turn Up
BotPath.add_turn(90,rate=0.5,step_number=20,color=pu.blue)

BotPath.savefig(save_path+'TestFile.png')

BotPath.show()

