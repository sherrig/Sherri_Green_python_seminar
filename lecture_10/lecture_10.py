# Title: Lecture 10 Individual Script#
# Lesson: Biot-Savart's Law     #
# Filename: lecture_10.py         #
# Original Author: Joe Griffin  #
# Most Recent Edit: 3/2/2014   #
# Last Editor: PR      #
#################################

# This script calculates the magnetic field of a current-carrying ring at a distance
#   z above the ring, on the central axis of the ring.

import numpy as np
from math import sin, cos, pi
from const import mu0
dtheta = 1e-4                                       # Integral Precision

I = 10.0                                            # Ring Properties I in amp, R in m
R = 0.5

def B(z):                                           # For the moment, we only vary z
    P = np.array((0.0, 0.0, z))
    B = np.array((0.0, 0.0, 0.0))
    for i in xrange(int(2 * pi / dtheta)):
            theta = i * dtheta
            pos = R * np.array((cos(theta),         # Location of differential current
                                sin(theta),
                                0.0))
            r = P - pos
            r_mag = np.linalg.norm(r)
            dl = R * dtheta * np.array((-sin(theta),# Differential wire vector, a positive current flows CCW from the top
                                        cos(theta),
                                        0.0))
            dB = (mu0 * I * np.cross(dl, r) /       # Invoke Biot-Savart Law
                  (4.0 * pi * r_mag**3))
            B = B + dB
    return B

def analyticalB(z):
    B_z = ((mu0 * I * R**2) /
           (2.0 * (z**2 + R**2)**(3 / 2.0)))
    return np.array((0, 0, B_z))
