#################################
# Title: Lecture 4 Group Script #
# Lesson: Gauss' Law            #
# Filename: group_4.py	        #
# Original Author: Joe Griffin	#
# Most Recent Edit: 1/23/2015	#
# Last Editor: Joe Griffin	#
#################################

# We will calculate the electric field due to a non-uniformly charged rod in space.
# We use direct integration and use symmetry to reduce it to a 1D scalar integral.

from math import sqrt, pi, cos
from const import E0
k = 1.0 / (4 * pi * E0)

def lamda(x):
    return 1e-5 * cos(x)

# here dE_list is the y-component of the electric field because we relized that the other
# components are zero

def E(yp):
    rod = ((-4.0, 0.0, 0.0), (4.0, 0.0, 0.0))           # Endpoint 1, endpoint 2
    L = sqrt((rod[1][0] - rod[0][0])**2)                # Length of rod
    dx = 1.0e-3                                         # Integral increment length
    
    dE_list = []                                        # differential contributions
    for i in xrange(int(L / dx)):                       # Create our integration iterable
        dq = lamda((i * dx) - (L / 2)) * dx
        pos = rod[0][0] + ( i * dx)                     # Pos is x-coord of dq
        r = sqrt(yp**2+ (pos)**2)                      # r is distance from pos to P=(0,yp,0)
        dE = k * dq / (r**2)                            #magnitude if the E-field vector due to dq at point P
        dE_list.append(dE * yp / r)
    E = sum(dE_list)                                    # Total E
    return E
