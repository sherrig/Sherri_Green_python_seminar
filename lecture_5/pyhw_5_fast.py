#################################
# Title: Py Homework 5 Fast     #
# Lesson: Electric Potential    #
# Filename: pyhw_5_fast.py	#
# Original Author: Joe Griffin	#
# Most Recent Edit: 1/17/2015	#
# Last Editor: Joe Griffin	#
#################################

# We will calculate the potential due to a charged semicircle along a line, then graph that
#   potential curve as a function of position.

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
    end = (Q[2] - ctr) / R                              # Direction across semicircle
    perp = (Q[1] - ctr) / R                             # Direction into semicircle
    dtheta = 1.0e-3                                     # Integral increment angle (precision)
    index = np.arange(int(pi / dtheta))
    theta = (index * dtheta) - (pi / 2)
    lFast = np.vectorize(lamda)
    dq = lFast(theta) * dtheta * R
    sinFast = np.vectorize(sin)
    cosFast = np.vectorize(cos)
    ctrs = np.outer(np.ones((int(pi / dtheta), 1)), ctr)
    ends = np.outer(sinFast(theta), end) * R
    perps = np.outer(cosFast(theta), perp) * R
    pos = ctrs + ends + perps                           # pos is location in space of dq
    P_col = np.outer(np.ones((int(pi / dtheta), 1)), P)
    r = np.linalg.norm(P_col - pos, axis = 1)
    phi = k * np.sum(np.divide(dq, r))
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
