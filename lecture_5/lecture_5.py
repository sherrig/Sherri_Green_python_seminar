#################################
# Title: Lecture 5              #
# Lesson: Electric Potential    #
# Filename: lecture_5.py	#
# Original Author: Joe Griffin	#
# Most Recent Edit: 1/15/2015	#
# Last Editor: Joe Griffin	#
#################################

# Relevant Classes: 6.004

# We will calculate the potential due to a charged rod along a line, then graph that potential
#   curve as a function of position.

import time
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

start = time.time()
path = range(50)
V = []
for j in path:
    V.append(Phi(np.array([0.01, j / 20.0, j / 30.0])))

plot(path, V)
print start - time.time()
show()
