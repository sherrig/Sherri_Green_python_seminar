#################################
# Title: Homework 10 Script     #
# Lesson: Biot-Savart's Law     #
# Filename: pyhw_10_sol.py      #
# Original Author: Joe Griffin  #
# Most Recent Edit: 3/7/2014    #
# Last Editor: Joe Griffin      #
#################################

# This script calculates the magnetic field of a current-carrying ring and  solenoid at a given
# point in space. It compares B far away from a ring with the analytical solution in the yz plane.

import numpy as np
from math import sin, cos, pi, sqrt
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
from const import mu0
dtheta = 1e-3                                       # Integral Precision

I = 10.0                                            # Ring Properties I in amp, R in m
a = 0.5

# B of a ring located at height z, evaulated at a generic location

def B(P, z):                                        # We now move the point anywhere in space,
    B = np.array((0.0, 0.0, 0.0))                   #   and let the ring's z-coordinate vary.
    for i in xrange(int(2 * pi / dtheta)):
        try:
            theta = i * dtheta
            pos = a * np.array((cos(theta),         # Location of differential current
                                sin(theta),
                                z / a))
            r = P - pos
            r_mag = np.linalg.norm(r)
            dl = a * dtheta * np.array((-sin(theta),# Positive current flows CCW from the top
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


# Analytical B far away from a ring located at the origin

def analyticalBFar(P):
    d = sqrt (P[1]**2 + P[2]**2)                               # distance from the center of the ring
    B_y = mu0 * I / (4 * pi) * 3 * pi * a**2 * P[1] * P[2]/ d**5    # y component
    B_z = mu0 * I / (4 * pi) * pi * a**2 / d**3 * ( 2 - 3 * P[1]**2/d**2) # z component
    return np.array((0, B_y, B_z))

def solenoid_B(a, N, L, P):                         # Assume solenoid starts at origin and
    B = np.array((0.0, 0.0, 0.0))                   #   is oriented along z-axis
    try:
        for turn in xrange(N):
            ring_B = B(P, turn * L / (N-1) )        # Each ring contributes a significant amount
    except KeyboardInterrupt:                       #   to the total, so losing one ring ruins
        print 'Loop number: ' + str(N)              #   the calculation. We have to retry if
                                                    #   we impatiently interrupt Python. 
#    except ZeroDivisionError:
#        print "If you're only evaluating one "+ \  
#             "ring, just use the single-ring "+ \ # If   Python goes forever, though, we interrupt.
#              "function."
    else:                                           
        B += ring_B                                 
    return B



#Will calculate the numerical and the theoretical magnitude of B for distances larger than a
path = range(60)
dis = [] # distance from the origin normalized to the radius a
err = []              #absolute value of the relative error

for j in path:
    P = np.array([0.0, j/20. , 0.1])
    num = np.linalg.norm(B(P,0))
    th = np.linalg.norm(analyticalBFar(P))
    distance = np.linalg.norm(P)/a
    if distance > 1:
        err.append(abs((num-th)/th))
        dis.append((np.linalg.norm(P)/a))
      
	


# Calculate the maximum and minimum of the magnitude of the error

ma = max(err)
print 'Maximum value of the relative error=', ma


mi = min(err)
# locMin = np.argmin(err) 
print 'Minimum value of the relative error=', mi 

plt.plot(dis,err,'r--')
plt.grid(True)
plt.xlabel(' r/a')
plt.ylabel('  |num(r)-th(r)/th(r)|')

plt.show()

