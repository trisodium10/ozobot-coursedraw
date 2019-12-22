import numpy as numpy
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

"""
ipython execution
%run '/home/hayman/python/ozobot/testscripts/01_test_draw.py'
"""

red=(1, 0, 0, 1)
blue=(0, 0, 1, 1)
green=(0, 1, 0, 1)
black=(0, 0, 0, 1)

figsize = (4,5) # size of figure in inches
xlimits=[0,figsize[0]]
ylimits=[0,figsize[1]]

fig,ax = plt.subplots(1,1,figsize=figsize)
fig.tight_layout()


save_path = None

rect = Rectangle((2,3),0.1275,0.1275,fill=True,color=black)
ax.add_patch(rect)

ax.set_xlim(xlimits)
ax.set_ylim(ylimits)
ax.axis('off')

if save_path is None:
    plt.show()
else:
    plt.savefig(save_path+"test.png", bbox_inches='tight')
