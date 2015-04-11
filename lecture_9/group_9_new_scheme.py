#################################
# Title: Lecture 9 Group Script Runge Kutta #
# Lesson: Magnetic Field/Force  #
# Filename: group_9_new_scheme.py	        #
# Original Author: Analia Barrantes	#
# Most Recent Edit: 2/6/2014	#
# Last Editor: AB	#
#################################

# This script calculates positions, velocities, and accelerations as numpy arrays and
#   records tuples of those data in a text file to read into VPython elsewhere.
# This script uses the Runge Kutta integration method (read extra notes)


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
Np = 15 									# Number of periods
dt = T /1000                                # 1000 points in one period

numPoints = Np * int ( T /dt)                          


print "mag B",B_mag
print "R", R
print "v_p", v_p
print "Period", T
print "dt", dt
print "Number of periods", Np
print "number of iterations", numPoints

h = q * B_mag / (2 * m) #parameter introduced to simplify the notation


# Start  calculations 

pos=[]
vel=[]
cc1=[]

p = startPos
v = (startVel)
f = np.cross(q * v, B)
a = f / m
xo = startPos[0]
zo = startPos[2]
x1 = startPos[0] + startVel[0] * dt + 0.5 * a[0] * dt * dt
z1 = startPos[2] + startVel[2] * dt + 0.5 * a[2] * dt * dt
     
for iteration in xrange(numPoints):

    t = dt * iteration
    c1 = 2 * x1 - xo + zo * h * dt
    c2 = 2 * z1 - zo - xo * h * dt
    x2 =   (c1 - h * dt * c2)/(1 + (h * dt)**2 )
    z2 =   (c1 * h * dt + c2)/(1 + (h * dt)**2 )
    y2 = 0.

    pos.append([x2, 0, z2])
    vel.append(v)

    xo = x1                     # Reset
    zo = z1
    x1 = x2
    z1 = z2	
     
    
    
# If we want to plot to see things are OK  Define the np.arrays

pos_a = np.array(pos)
vel_a = np.array(vel)

#  PLot


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
plot((vel_a[:,0]**2+vel_a[:,1]**2+vel_a[:,2]**2)**0.5)
title("Kinetic energy vs time")
show()


show()
