#################################
# Title: Lecture 9 Group Script #
# Lesson: Magnetic Field/Force  #
# Filename: group_9.py          #
# Original Author: Joe Griffin  #
# Most Recent Edit: 2/6/2014    #
# Last Editor: Joe Griffin      #
#################################

# This script calculates positions, velocities, and accelerations as numpy arrays and
#   records tuples of those data in a text file to read into VPython elsewhere.

import numpy as np
dt = 1e-3                                           # Simulator Settings
numPoints = 1e4

m = 1e-22                                           # Particle Properties
q = 1.6e-19

startPos = np.array((0.0, 0.0, 0.0))                # Initial Conditions
startVel = np.array((10.0, 0.3, 0.))

B = np.array((0., 1e-3, 0.))                        # Environmental Conditions

with open('traj.txt', 'w', 0) as text:              # Open a writeable text file
    p = startPos                                    # Copy/paste w/o `with` then indent & add file I/O
    v = startVel
    for iteration in xrange(numPoints):
        t = dt * iteration
        f = np.cross(q * v, B)                      # Magnetic force calculation
        a = f / m                                   # Side idea: add a friction term! :)
        v = v + a * dt                              # Integrals
        p = p + v * dt
        pVec = p.tolist()                           # This will make reading from the
        vVec = v.tolist()                           #   file much nicer.
        aVec = a.tolist()
        text.write(str((pVec, vVec, aVec)) + '\n')  # Data dump
