#################################
# Title: Lecture 5 Group Script #
# Lesson: Electric Potential    #
# Filename: group_5.py	        #
# Original Author: Joe Griffin	#
# Most Recent Edit: 1/22/2015	#
# Last Editor: Joe Griffin	#
#################################

#Consider a rod of length L = 1 m and with a uniform linear charge
#density of λ=3e-5 C/m. The rod is vertical, along the y-axis.
#The bottom end is at the origin and the top one is at (0, 1, 0) m.
#Calculate and graph the electric potential  (wrt infinity) along the line segment connecting
#points (1, 2, 2) and (1.5, 0.5, 1).

from math import sqrt, pi
from const import E0
from matplotlib.pyplot import *
k = 1.0 / (4 * pi * E0)

def Phi(P):
    lamda = 3e-5

    rod = ((0.0, 0.0, 0.0), (0.0, 1.0, 0.0))            # Endpoint 1, endpoint 2
    L = sqrt(((rod[1][0] - rod[0][0])**2) +             # Length of rod
             ((rod[1][1] - rod[0][1])**2) +
             ((rod[1][2] - rod[0][2])**2)
             )
    rod_x = (rod[1][0] - rod[0][0]) / L                 # x, y, z components of rod vector
    rod_y = (rod[1][1] - rod[0][1]) / L
    rod_z = (rod[1][2] - rod[0][2]) / L
    dy = 1.0e-3                                         # Integral increment length (precision)

    phi = 0.0                                           # Electrostatic Potential
    for i in xrange(int(L / dy)):                       # Create our integration iterable
        dq = lamda * dy
        pos_x = 0                                       # Pos is location in space of dq. 
        pos_y = rod[0][1] + (rod_y * i * dy)            
        pos_z = 0
        r = sqrt(((P[0] - pos_x)**2) +                  # r is distance from pos to P
                 ((P[1] - pos_y)**2) +
                 ((P[2] - pos_z)**2)
                 )
        phi += k * dq / r

    return phi

V = []
path = range(500)
for step in path:
    V.append(Phi((1 + (step / 1e3),
                  2 - (3 * (step / 1e3)),
                  2 - (step / 500.0)
                  )))
plot(path, V)
show()
