#################################
# Title: Lecture 10 Group Script#
# Lesson: Biot-Savart's Law     #
# Filename: group_10.py         #
# Original Author: Joe Griffin  #
# Most Recent Edit: 2/28/2014   #b
# Last Editor: Joe Griffin      #
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
        try:
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
        except KeyboardInterrupt:                   # A prime example of good exception
            print 'theta =', i * dtheta             #   handling: status updates
            prompt = 'Continue execution? (Y/N) '
            persevere = raw_input(prompt)
            if not persevere.lower()[0] == 'y':
                msg = 'Iteration Limit Exceeded'
                raise Exception(msg)
    return B

def analyticalB(z):
    B_z = ((mu0 * I * R**2) /
           (2.0 * (z**2 + R**2)**(3 / 2.0)))
    return np.array((0, 0, B_z))

try:
    for j in range(5):
        Bc = B(j / 5.0)
        Ba = analyticalB(j / 5.0)
        error = (np.linalg.norm(Ba - Bc) /
                 np.linalg.norm(Ba))
        assert error < 0.01                         # Error must be less than 1%

except AssertionError:
    print 'Bc =', Bc                                # What else can we print here? e.g. location
    print 'Ba =', Ba
    print 'Error =' + str(100 * error) + '\%'

except Exception as e:
    print 'Error message:', e.message

else:
    print 'B(z) behaves as expected. Proceed.'
