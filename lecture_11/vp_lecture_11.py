#################################
# Title: Lecture 11               #
# Lesson: Coil gun               #
# Filename: vp_lecture_11.py
# Original Author: Paola Rebusco #
# Created: 3/27/2015
# Most Recent Edit: 3/27/2015	  #
# Last Editor: PR	          #
#################################

#This script calculates and shows the magnetic field of a solenoid 


from __future__ import division
from visual import color,curve, arrow, ring, vector, label, scene, rate
import numpy as np
from math import sin, cos, pi, sqrt
from const import mu0


scene.center = (0, 0, 0.5)                  # re- center the scene 
scene.forward = vector(-0.5, 0.05, - 0.2)     # tilt the initial scene

#Draw a coordinate system
#. Draw the (x,y,z) coordinate system - label (0,0,0)
a = 0.3                       #length of the (x,y,z) axis
arrow(pos = vector(0.6,-0.6,1.2),axis = vector(a/2,0,0), shaftwidth = 0.01, color = color.white)
arrow(pos = vector(0.6,-0.6,1.2),axis = vector(0,a/2,0), shaftwidth = 0.01, color = color.white)
arrow(pos = vector(0.6,-0.6,1.2),axis = vector(0,0,a/2), shaftwidth = 0.01, color = color.white)
label(pos = vector(0.5,-0.6,1.), xoffset = -.5,yoffset = -0.5, zoffset = -.5,text='O',box = False,background = color.white,opacity = 0.06, line = False)
label(pos = vector(0.6+a/2,-0.6,1.2), xoffset = -a/6,yoffset = +a/6, text = 'x',box = False,background = color.white,opacity = 0.06, line = False) 
label(pos = vector(0.6,a/2-0.6,1.2), xoffset = a/6,yoffset = a/10, text = 'y',box = False, background = color.white,opacity = 0.06, line = False) 
label(pos = vector(0.6,-0.6, a/2+1.2), xoffset = -a/6,yoffset = a/6,zoffset = -a/6, text = 'z',box = False, background = color.white,opacity = 0.06, line = False) 



#Draw the solenoid

ra = 0.5 # 5 cm radius (we decide the units for nicer visualization)
l = 1 # 10 cm length
N = 30


for i in xrange(N+1):
   ring(pos = (0,0,l *i / float(N)), axis = (0,0,1), radius = ra\
        ,thickness = 0.02, color = color.yellow, opacity = 0.3)




# function to calculate B of a solenoid composed by the two rings taken from group_11.py

I = 10 # current in the solenoid
dtheta = 5*1e-3  # integral precision


def solenoid(P, N, l):                              # B of solenoid length l from origin loops N at P
    interval = int(2 * pi / dtheta)
#    interval = 5   # for debug
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



# Draw the magnetic field produced by the solenoid

scale = 8.e-2
v = 20

for i in xrange(v):
   vec = solenoid((0,0, (l+0.5)*i/(v-1) - 0.2),N,l)
   magn = np.linalg.norm(vec)  
   arrow(pos = vector(0,0,(l+0.5)*i/(v-1) - 0.2),axis = scale*vec/magn,shaftwidth = 0.01, color = color.orange)
   for j in xrange(10):
        loc = (0.1*cos(2*pi*j/9),0.1*sin(2*pi*j/9), (l+0.5)*i/(v-1) - 0.2)
        vec = solenoid(loc,N,l)
        magn = np.linalg.norm(vec) 
        arrow(pos = vector(loc), axis = scale*vec/magn,shaftwidth = 0.01, color = color.orange)
        loc = (0.2*cos(2*pi*j/9),0.2*sin(2*pi*j/9), (l+0.5)*i/(v-1) - 0.2)
        vec1 = solenoid(loc,N,l)
        magn1 = np.linalg.norm(vec1)  
        arrow(pos = vector(loc),axis = scale*vec1/magn1,shaftwidth = 0.01, color = color.orange)
        loc = (0.3*cos(2*pi*j/9),0.3*sin(2*pi*j/9), (l+0.5)*i/(v-1) - 0.2)
        vec1 = solenoid(loc,N,l)
        magn1 = np.linalg.norm(vec1)  
        arrow(pos = vector(loc),axis = scale*vec1/magn1,shaftwidth = 0.01, color = color.orange)

