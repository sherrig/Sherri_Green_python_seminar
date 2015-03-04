#################################
# Title: Lecture 5  Visual part             #
# Lesson: Electric Potential visualization   #
# Filename: vp_lecture_5.py	#
# Original Author: Joe Griffin	#
# Most Recent Edit: 1/27/2015	#
# Last Editor: PR	#
#################################

# Relevant Classes: 6.004

# We will calculate the potential due to a charged rod along a line, then graph that potential
#   curve as a function of position. Visualize the rod and the trajectory
# along which we plot phi using nice colors

from __future__ import division
from visual import cylinder,color,local_light,curve
import numpy as np
from matplotlib.pyplot import plot, show
from math import sqrt, pi, exp
from const import E0

k = 1.0 / (4 * pi * E0)


def lamda(d):
    return exp(-((d - 0.5)**2) / 0.01) * 1e-8

def Phi(P):
    rod = (np.array([0.0, 0.0, 0.0]),                   # Endpoint 1, endpoint 2
           np.array([0.0, 1.0, 0.0])
           )
    
    rod_vec = rod[1] - rod[0]
    L = np.linalg.norm(rod_vec)                         # np.linalg.norm() calculates vector
                                                        #   magnitude, which is handy here
    
    rod_dir = rod_vec / L                               # rod direction vector
    dy = 1.0e-4                                         # Integral increment length (precision)

    phi = 0.0                                           # Electrostatic Potential
    for i in xrange(int(L / dy)):                       # Create our integration iterable
        dq = lamda(i * dy) * dy
        pos = rod[0] + (rod_vec * i * dy)               # Pos is location in space of dq
        r = np.linalg.norm(P - pos)
        phi += k * dq / r
    return phi




#visualize the rod with colors as a function of the charge density

n=50

rod= range(n)

for i in rod:
    c = (lamda((i+1)/n) / lamda(0.5), 0.3, 0) 
    cylinder(pos = (0,i/(n-1),0), axis = (0,1/n,0), radius = 0.01, color=c)

# Graph the trajectory we’re plotting the potential along:
# color the trajectory according to the potential at each point 


# plot the potential along the trajectory

path = range(50)
V = []
for j in path:
    loc = Phi(np.array([0.01, j / 20.0, j / 30.0]))
    V.append(loc)
    c = (0,0,loc/60)
    curve(pos = [(0.01, j / 20.0, j / 30.0),(0.01, (j+1) / 20.0, (j+1) / 30.0)],color=c,radius=0.005)

#plot(path, V)
#show()


