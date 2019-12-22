
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

"""
RGBA Color Definitions
"""
red=(1, 0, 0, 1)
blue=(0, 0, 1, 1)
green=(0, 0.6, 0, 1)
black=(0, 0, 0, 1)

# block size in inches
step_size = 0.1275

"""
Function Definitions
"""
def make_step(loc,color,angle=0):
    """
    Draw a block for a given color
    inputs:
        loc - (x,y) location on plot
        color - RGBA definition

    return:
        patches object that can be added to
            the subplot using
            ax.add_patch()
    """
    angle = np.mod(angle,90)
    loc_adj = (loc[0]-np.sqrt(2)*step_size/2*np.cos((angle+45)*np.pi/180),
                loc[1]-np.sqrt(2)*step_size/2*np.sin((angle+45)*np.pi/180))
    rect = Rectangle(loc_adj,step_size,step_size,fill=True,color=color,angle=angle)
    return rect

class Ozo_Path:
    def __init__(self,figsize):
        """
        Create an Ozo_Path figure with size
        in inches defined by figsize in (x,y)
        """
        self.xlimits=[0,figsize[0]]
        self.ylimits=[0,figsize[1]]

        self.fig,self.ax = plt.subplots(1,1,figsize=figsize)
        self.fig.tight_layout()

        
        self.ax.axis('equal')
        self.ax.set_xlim(self.xlimits)
        self.ax.set_ylim(self.ylimits)
        self.ax.axis('off')

        self._step_pointer = np.array([0,0])
        self._step_direction = np.array([1,0])
        self._angle = 0

    def add_step(self,color,count=1):
        """
        Add a step of a specified RGBA color
        to the current step_pointer location
        """
        counter = 0
        while counter < count:
            step = make_step(self._step_pointer,color,angle=self._angle*180/np.pi)
            self.ax.add_patch(step)  # add the step to the board
            # increment the step in the current direction
            self._step_pointer = self._step_pointer+self._step_direction*step_size
            counter+=1

    def set_position(self,loc):
        self._step_pointer = np.array(loc)

    def set_direction(self,angle):
        self._angle = angle*np.pi/180
        self._step_direction = np.array([np.cos(self._angle),np.sin(self._angle)])

    def set_rel_direction(self,angle):
        self.set_direction(self._angle*180/np.pi+angle)

    def add_fast(self):
        self.add_step(blue)
        self.add_step(black)
        self.add_step(blue)

    def add_slow(self):
        self.add_step(red)
        self.add_step(black)
        self.add_step(red)

    def show(self):
        #self.ax.axis('equal')
        self.fig.show()

    def savefig(self,filename):
        self.fig.savefig(filename, bbox_inches='tight')