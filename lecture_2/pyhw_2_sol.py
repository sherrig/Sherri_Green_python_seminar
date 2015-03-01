#################################
# Title: Py Homework 2 Solution	#
# Lesson: Point Charges Field   #
# Filename: pyhw_2_sol.py	#
# Original Author: Joe Griffin	#
# Most Recent Edit: 1/13/2014	#
# Last Editor: Joe Griffin	#
#################################

# This script gives an example of the code for a function that calculates the electric field
#   at an arbitrary point of an arbitrarily placed charge.

from math import sqrt, pi                               # Gather constants and functions
from const import E0
k = 1.0 / (4 * pi * E0)

def E(q, P):
    r = (P[0] - q[0], P[1] - q[1], P[2] - q[2])
    mag = sqrt((r[0]**2) + (r[1]**2) + (r[2]**2))
    field = []
    field.append(k * (r[0] / mag) * (q[3] / (mag**2)))  # Calculate x, y, and z components
    field.append(k * (r[1] / mag) * (q[3] / (mag**2)))
    field.append(k * (r[2] / mag) * (q[3] / (mag**2)))
    return field
