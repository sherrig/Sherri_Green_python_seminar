#################################
# Title: Lecture 9 Group Script #
# Lesson: Magnetic Field/Force  #
# Filename: group_9.py	        #
# Original Author: Joe Griffin	#
# Most Recent Edit: 2/6/2014	#
# Last Editor: Joe Griffin	#
#################################

# This script calculates positions, velocities, and accelerations as numpy arrays and
#   records tuples of those data in a text file to read into VPython elsewhere.


from matplotlib.pyplot import plot, show

import numpy as np
from math import pi,sqrt
from matplotlib.pyplot import plot, title, show, grid, subplot



startPos = np.array((0,0, 0))               # Initial Conditions
startVel = np.array((10,2., 0))

B = np.array((0,1e-3,0))                      # Environmental Conditions
B_mag = np.linalg.norm(B)                    # magnitude of B (In T)

m = 1e-22                                            # Particle Properties ([m]=kg, [q]=C)
q = 1.6*1e-19

v_p = sqrt( startVel[0]**2 + startVel[2]**2 )     # component of the velocity in the 
											      # direction perpendicular to the B-filed 
											
R = m * v_p/(abs(q) * B_mag)                # Radius of the orbit [R] = m
T = 2. * pi * m / (abs(q) * B_mag)          # Period [T[]= s
Np = 3  									# Number of periods
#dt = 1e-3                                                # Simulator Settings
dt = T /1000                                # 1000 points in one period

numPoints = Np * int ( T /dt)                          


print "mag B",B_mag
print "R", R
print "v_p", v_p
print "Period", T
print "dt", dt
print "Number of periods", Np
print "number of iterations", numPoints


# Start  calculations and  storage

pos=[]
acc=[]
vel=[]
force=[]

with open('traj1.txt', 'w', 0) as text:              # Open a writeable text file
    p = startPos
    v = (startVel) 
    for iteration in xrange(numPoints):
        t = dt * iteration
        f = np.cross(q * v, B)                      # Magnetic force calculation
        a = f / m
		
        v = v + (a * dt)                            # Integrals
        p = p + (v * dt)


        pVec = p.tolist()                           # This will make reading from the
        vVec = v.tolist()                           #   file much nicer.
        aVec = a.tolist()
        text.write(str((pVec, vVec, aVec)) + '\n')  # Data dump
        pos.append(p)
        acc.append(a)
        vel.append(v)
        force.append(f)
    
    
# If we want to plot to see things are OK  Define the np.arrays

pos_a = np.array(pos)
acc_a = np.array(acc)
vel_a = np.array(vel)
force_a=np.array(force)

subplot(221)
grid(True)
plot(pos_a[:,0]/R)
title("x/R vs t")

subplot(222)
grid(True)
plot(pos_a[:,0]/R,pos_a[:,2]/R)
title('z/R vs x/R')

subplot(212)
grid(True)
plot(( vel_a[:,0]**2 + vel_a[:,1]**2+vel_a[:,2]**2 )**0.5 )
title("Kinetic energy vs time")
show()
