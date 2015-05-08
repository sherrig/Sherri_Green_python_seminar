#################################
# Title: Homework 11 Script     #
# Lesson: Faraday's Law         #
# Filename: pyhw_11_sol.py      #
# Original Author: Joe Griffin  #
# Most Recent Edit: 3/27/2014   #
# Last Editor:             PR   #
#################################

# This script calculates the magnetic flux of a pair of current-carrying rings through
#   a rotating square loop in a generator format, then plots it against the approximate
# value (obtained for B~const).

import numpy as np
from math import sin, cos, pi, sqrt
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
from const import mu0
import time

dtheta = 1e-3                                       # Integral Precisions
dx = 1e-2
dy = 1e-2
res = 10.0                                          # Plotting resolution

I = 10.0                                            # current in the square loop (amp)
a = 0.05                                            # radius of the rings in m

def solenoid(P, N, l):                              # B of solenoid length l from origin loops N at P
    interval = int(2 * pi / dtheta)
    i = np.outer(np.ones((N,)),
                 np.arange(interval)
                 )                                  # i.shape = (N, interval)
    theta = dtheta * i                              # theta.shape = (N, interval)
    z = np.outer(l * np.arange(N) / float(N - 1),
                 np.ones((interval,))
                 )
    pos = a * np.array((np.cos(theta),
                        np.sin(theta),
                        z / a
                        ))                          # pos.shape = (3, N, interval)
    P_mat = np.outer(P, np.ones((N, interval)))
    P_matrix = np.reshape(P_mat, (3, N, interval))  # P_matrix.shape = (3, N, interval)
    r = P_matrix - pos                              # r.shape = (3, N, interval)
    r_mag = np.linalg.norm(r, axis = 0)             # r_mag.shape = (N, interval)

    dl_components = (np.reshape(-np.sin(theta),
                                (N, interval, 1)),
                     np.reshape(np.cos(theta),
                                (N, interval, 1)),
                     np.zeros((N, interval, 1))
                     )
    dl_array = np.concatenate(dl_components,        # want: dl.shape = (3, N, interval)
                              axis = 2
                              )
    dl = a * dtheta * np.transpose(dl_array,        # dl.shape = (3, N, interval)
                                   axes = (2, 0, 1)
                                   )
    num = mu0 * I * np.cross(dl, r, axis = 0)
    denom = 4.0 * pi * r_mag**3
    dB = num / denom                                # Invoke Biot-Savart Law
    B = np.sum(dB, axis = (1, 2))
    return B

def generatorFlux(phi):                             # Flux through loop at angle phi (angle between B and vector area)
    ctr = np.array((0.0, 0.0, 0.05))
    S = 0.5 * a                                      # Side of the loop
    Flux = 0
    for i in xrange(int(S / dx)):                   ### Polar coordinates for easy limits
        for j in xrange(int(S / dy)):
#            x = i * dx - S / 2
#            y = j * dy - S / 2
#            shift = S * np.array((x,                # what is this? units?
#                                  y,
#                                  S * sin(phi)
#                                  ))
            x = i * dx - S / 2
            y = (j * dy - S / 2) * cos(phi)
            z = (j * dy - S / 2) * sin(phi)
            shift = np.array((x, y, z))          # location inside the loop wrt to the center
            
            pos = ctr + shift
            dA = dx * dy * np.array((0.0,           # Differential area vector
                                     -sin(phi),
                                     cos(phi)
                                     ))
            B = solenoid(pos, 2, 0.1)
            dF = np.dot(B, dA)
            Flux += dF
    return Flux

# Make a plot for phi in (0, 2pi)

angle = np.arange(int(2 * pi * res)) / res
flux = []
start = time.time()
for phi in angle:                                   # Create iterables for plotting
    try:
        flux.append(generatorFlux(phi))
        print 'Angle', phi, 'complete.'
        print 'Current runtime:', time.time() - start
    except KeyboardInterrupt:
        print 'Angle:', phi
        print 'Runtime:', time.time() - start, '\n'
print 'Total Runtime:', time.time() - start
plot(angle, flux, 'ob')
plot(angle, max(flux) * np.cos(angle), '*r')
title('Numerical calculation VS Uniform Field Comparison')
xlabel('Rotation Angle in rad')
ylabel('Flux in Tesla')
show()
