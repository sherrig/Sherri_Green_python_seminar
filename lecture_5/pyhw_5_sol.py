#################################
# Title: Py Homework 5 Solution #
# Lesson: Electric Potential    #
# Filename: pyhw_5_sol.py	#
# Original Author: Joe Griffin	#
# Most Recent Edit: 1/22/2015	#
# Last Editor: Joe Griffin	#
#################################

# We will calculate the potential due to a charged semicircle along a line, then graph that
#   potential curve as a function of position (see homework 5 for details).

import numpy as np
from matplotlib.pyplot import plot, show
from math import sqrt, pi, exp, sin, cos
from const import E0
k = 1.0 / (4 * pi * E0)


def lamda(theta):
    return 1e-6 / (1 + exp(-5 * (theta - pi/2)))

def Phi(P):
    Q = (np.array([0, 0, 0]),                           # (End 1, middle, end 2)
         np.array([0.5, 0, 0.5]),
         np.array([0, 0, 1])
         )
    R = np.linalg.norm(Q[2] - Q[0]) / 2
    ctr = (Q[0] + Q[2]) / 2.0
    end = (Q[2] - ctr) / R                              # Direction across semicircle (+z-dir)
    perp = (Q[1] - ctr) / R                             # Direction into semicircle   (+x-dir)
    dtheta = 1.0e-3                                     # Integral increment angle (precision)

    phi = 0.0


    # Electrostatic Potential
    for i in xrange(int(pi / dtheta)):                  # Create our integration iterable
        theta = (i * dtheta) - (pi / 2)
        dq = lamda(theta) * R * dtheta
        ends = sin(theta) * end * R
        perps = cos(theta) * perp * R
        pos = ctr + ends + perps
        r = np.linalg.norm(P - pos)
        phi += k * dq / r
    return phi

path = range(50)
V = []
for j in path:
    P = np.array([0.0 + (j / 50.0),
                  0.25 - (j / 100.0),
                  0.0 + (j / 100.0)
                  ])
    V.append(Phi(P))

plot(path, V)
show()
