#################################
# Title: Lecture 11               #
# Lesson: Generator                #
# Filename: animation_generator_11.py	  #
# Original Author: Paola Rebusco #
# Most Recent Edit: 3/27/2015	  #
# Last Editor: PR	          #
#################################



from __future__ import division
from visual import color,curve, arrow, ring, vector, label, scene, rate
import numpy as np
from math import sin, cos, pi, sqrt
from const import mu0


scene.center = (0, 0, 0.5)                  # re- center the scene 
scene.forward = vector(-0.3, 0.05, - 0.2)     # tilt the initial scene

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



#Draw the two electromagnets

ra = 0.5 # 5 cm radius

loop1 = ring(pos = (0,0,0), axis = (0,0,1), radius = ra, thickness = 0.02, color = color.yellow)
loop2 = ring(pos = (0,0,1), axis = (0,0,1), radius = ra, thickness = 0.02, color = color.cyan)



# function to calculate B of a solenoid composed by the two rings taken from group_11.py

I = 10 # current in the solenoid
dtheta = 1e-3  # integral precision

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



# Draw the magnetic field produced by the two rings

scale = 1.e4
v = 5

for i in xrange(v):
 arrow(pos = vector(0,0, i/v),axis = scale*solenoid((0,0, i/v),2,1),shaftwidth = 0.01, color = color.orange)
 for j in xrange(7) :
       loc = (0.25*cos(2*pi*j/6),0.25*sin(2*pi*j/6), 0.05+i/v)
       arrow(pos = vector(loc),\
             axis = scale*solenoid((loc),2,1),shaftwidth = 0.01, color = color.orange)
       loc = (0.5*cos(2*pi*j/6),0.5*sin(2*pi*j/6), 0.05+i/v)
       arrow(pos = vector(loc),\
             axis = scale*solenoid((loc),2,1),shaftwidth = 0.01, color = color.orange)

scene.autoscale = False # this is to avoid moving the camera bak and forth

#Draw the spinning square loop and its normal

n = 300

square = range(n)
normal = range(n)

rr = 0.25  # 2.5 cm radius

square[n-1] = curve(pos=[(rr/2,rr/2,0.5), (rr/2,-rr/2,0.5),(-rr/2,-rr/2,0.5),\
                         (-rr/2,rr/2,0.5),(rr/2,rr/2,0.5)],\
                         radius = 0.02, color = color.red)
normal[n-1] = arrow(pos = vector(0,0,0.5),axis = (0,0,0.3), shaftwidth = 0.02, color = color.green)

for i in xrange(n):
    rate(20)
    spin = (0, - 0.3*sin(i*2*pi/100), 0.3*cos(i*2*pi/100))
    square[i-1].visible = False
    normal[i-1].visible = False
    square[i] = curve(pos =[(rr/2,rr/2*cos(i*2*pi/100),0.5 + rr/2*sin(i*2*pi/100)), \
                          (rr/2,-rr/2*cos(i*2*pi/100),0.5 - rr/2*sin(i*2*pi/100)),\
                          (-rr/2,-rr/2*cos(i*2*pi/100),0.5 - rr/2*sin(i*2*pi/100)),\
                          (-rr/2,rr/2*cos(i*2*pi/100),0.5 + rr/2*sin(i*2*pi/100)),\
                            (rr/2,rr/2*cos(i*2*pi/100),0.5 + rr/2*sin(i*2*pi/100))], \
                    radius = 0.02, color = color.red)
    normal[i] = arrow(pos = vector(0,0,0.5),axis = spin, shaftwidth = 0.02, color = color.green)
    
