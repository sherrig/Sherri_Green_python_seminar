#################################
# Title: Py Homework 4 Solution #
# Lesson: Gauss' Law            #
# Filename: pyhw_4_sol.py	#
# Original Author: Joe Griffin	#
# Most Recent Edit: 1/23/2015	#
# Last Editor: Joe Griffin	#print flux
#################################

# We will calculate the force on a charged blanket due to a charged baby. This script
#   borrows the electric field function from homework 2.

import numpy as np
from matplotlib.pyplot import plot, show
from math import sqrt, pi, exp, sin, cos
from const import E0
k = 1.0 / (4 * pi * E0)

sigma = 0.001                                             # Charge Density of Blanket
baby = (0.0, 0.0, 0.0, 10**-6)                             # Baby charge
center = (0, 0, 1)                                      # Center of blanket
s = 2.0                                                 # Blanket sidelength
mass = 1.5                                              # Blanket weight in kilograms

def E(q, P):
    r = (P[0] - q[0], P[1] - q[1], P[2] - q[2])
    mag = sqrt((r[0]**2) + (r[1]**2) + (r[2]**2))
    field = []
    field.append(k * (r[0] / mag) * (q[3] / (mag**2)))  # Calculate x, y, and z components
    field.append(k * (r[1] / mag) * (q[3] / (mag**2)))
    field.append(k * (r[2] / mag) * (q[3] / (mag**2)))
    return field

flux = 0.0
dx = dy = 1e-3
z = center[2]
for step_x in xrange(int(s / dx)+1):
    x = (step_x * dx) - (s / 2.0) + center[0]
    for step_y in xrange(int(s / dy)):
        y = (step_y * dx) - (s / 2.0) + center[1]
        dA = dx * dy
        dq = sigma * dA
        E_z = E(baby, (x, y, z))[2]
        flux += E_z * dA                                # E * dA is our integrand

E_z_avg = flux / (s**2)
F_z = sigma * (s**2) * E_z_avg
F_g = 9.8 * mass
levitates = F_z > F_g
