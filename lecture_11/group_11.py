#################################
# Title: Group 11 Script        #
# Lesson: Faraday's Law         #
# Filename: group_11.py         #
# Original Author: Joe Griffin  #
# Most Recent Edit: 3/27/2014   #
# Last Editor: PR               #
#################################


#Consider a coil (a solenoid) of length L, radius a, loop count N.
#The bottom of the solenoid is on the xy-plane and the solenoid elongates along the z-axis.
#A current I flows (CCW from the top). Assume I = 10 amp, a = 2 cm.
# A coaxial loop of mass m = 1 g and radius R= a/2 is initially at the top of the solenoid.
#It carries a CW current I (same magnitude as the solenoid).
#Neglect induction. Neglect gravity.
#Calculate the velocity of the loop once it has travelled far enough
#that the magnetic field is negligible?
#We use `while` to decide when it’s far enough. All matrices generally short, fat (3 rows, many columns).

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
from const import mu0
import time

dtheta = 1e-3                                       # Integral Precision

I = 10.0                                            # Current of the solenoid and the projectile ring
a = 0.02                                            # Radius of the solenoid
# N = 100                                            # number of loops
# l = 0.1                                             # Length of the solenoid
R = a/2                                             # radius of the projectile ring 
m = 0.001                                            # 1 g projectile ring

# B of a ring located at height z, evaulated at a generic location P

def Bnp(P, z = 0):                                  # We now move the point anywhere in space,
    interval = int(2 * pi / dtheta)                 #   and let the ring's z-coordinate vary.
    i = np.arange(interval)                         # Differential Stage Count vector (no +1 b/c circ)
    theta = dtheta * i                              # Theta vector (radians)
    pos = a * np.array((np.cos(theta),              # Location of differential current
                        np.sin(theta),
                        z * np.ones((interval,)) / a
                        ))                          # pos.shape: 3 x interval
    r = np.outer(P, np.ones((interval,))) - pos     # r.shape: 3 x interval, P duplicated to
    r_mag = np.linalg.norm(r, axis = 0)             #   form P matrix, then pos subtracted
                                                     # axis = 0 specifies the column direction, to take the norm
                                                     # of each column, the result is 1 x interval
    dl = a * dtheta * np.array((-np.sin(theta),     # Positive current flows CCW from the top
                                np.cos(theta),        
                                np.zeros((interval,))
                                ))
    num = mu0 * I * np.cross(dl, r, axis = 0)       # Cross product in 3-space, not inf-space
    denom = 4.0 * pi * r_mag**3
    dB = num / denom                                # Invoke Biot-Savart Law
    B = np.sum(dB, axis = 1)                        # Axis argument returns a vector, not scalar
                                                    # axis = 1 add the elements of each row (the current elements
                                                    # in the ring
    return B


# B of a solenoid of length l, radius a, loop count N, at a generic location P.
# The bottom of the solenoid is on the xy plane and the solenoid is oriented along the z axis.
# A current I flows CCW from the top.

def solenoid(P, N, l):                              # B of solenoid length l from origin loops N at P
    interval = int(2 * pi / dtheta)
    i = np.outer(np.ones((N,)),
                 np.arange(interval)
                 )                                  # i.shape = (N, interval)
    theta = dtheta * i                              # theta.shape = (N, interval)
    z = np.outer(l * np.arange(N) / float(N - 1),  # location of the loops  
                 np.ones((interval,))
                 )
    pos = a * np.array((np.cos(theta),
                        np.sin(theta),
                        z / a
                        ))                          # pos.shape = (3, N, interval)
    P_mat = np.outer(P, np.ones((N, interval)))    # 3 by (N times interval)
    P_matrix = np.reshape(P_mat, (3, N, interval))  # P_matrix.shape = (3, N, interval)
    r = P_matrix - pos                              # r.shape = (3, N, interval)
    r_mag = np.linalg.norm(r, axis = 0)             # r_mag.shape = (N, interval)

    dl = a * dtheta * np.array((-np.sin(theta),     # dl.shape = (3, N, interval)
                                np.cos(theta),
                                np.zeros((N,interval))
                                ))                                
    num = mu0 * I * np.cross(dl, r, axis = 0)
    denom = 4.0 * pi * r_mag**3
    dB = num / denom                                # Invoke Biot-Savart Law
    B = np.sum(dB, axis = (1, 2))                   # we do not sum on axis =0 because that is the
                                                     # 3D space, axis = 1 is summing on N loops, axis =2
    return B                                          # sums on interval

# Final velocity of a current-carrying ring accelerated by the magnetic field of a
#   solenoid of length l, loops N, starting  at the origin and extending along the
#  z-axis.

def coilGun(N, l):                                  
    dt = 1e-3                                       # time integration interval 
    final_value_ratio = fvr = 1e-1                 # ratio between B(P) and B at the top of the solenoid  
    start_point = np.array((R,                      #the start point of a small piece of  the projectile ring     
                            0,                      
                            l * N / float(N - 1)   
                            ))                     
    B_init = solenoid(start_point, N, l)
    v = np.array((0.0, 0.0, 0.0))
    acc = np.array((0.0, 0.0, 0.0))
    ring_loc = l * N / float(N - 1)                 # Initial conditions of ring
    B, iteration, start = B_init, 0, time.time()    # generator assignment
    while np.linalg.norm(B / B_init) > fvr:         # Keep accelerating until magnetic field
         try:                                        #   decreases a few orders of magnitude.
            f = np.array((0.0,
                            0.0,
                            2 * pi * R * I * B[0]
                            ))
            ring_loc = ring_loc + v[2] * dt
            v += acc * dt
            acc = f / m                             
            B = solenoid(np.array((R, 0, ring_loc)), N, l)
            iteration += 1
    
         except KeyboardInterrupt:
             ratio = np.linalg.norm(B / B_init)
             print 'Ring state:', (ring_loc,
                                       v[2],
                                       acc[2]
                                       )
             print 'Field strength ratio:', ratio
             print 'Runtime =', time.time() - start
             print 'Iteration:', iteration, '\n'

    ratio = np.linalg.norm(B / B_init)
    print 'Ring final state:', (ring_loc,
                          v[2],
                          acc[2]
                          )
    print 'Final field strength ratio:', ratio
    print 'Total Runtime =', time.time() - start
    print 'Total number of iteration:s', iteration, '\n'
    print 'Final speed: ', np.linalg.norm(v), 'm/s'
    return 
