

from __future__ import division
from visual import *
import numpy as np
from math import pi


path = 'traj.txt'    
 

scene.title = "Path of charged particle in a B-field and E-field"              
scene.forward = vector(0, -.3, -1)                                  # to see the initial scene incline towards you




pos = []   # list to store x,y,z
vel = []   # list to store vx,vy,vz
acc = []   # list to store ax, ay, az

with open(path, 'r', 0) as traj:         
	line = traj.readline()                 # Data was entered line-by-line
	
	while line:
		raw_numbers = line.split(', ') # Print data is separated by comma-space		
		data = []

		for val in raw_numbers: # Convert all strings to floats
			data.append(float(val.strip('])([\n')))# Remove non-float characters from data		
	
		pos.append(data[0:3])
		vel.append(data[3:6])
		acc.append(data[6:9])
		line = traj.readline()

#Draw

wire = arrow(pos = (0,-20,0), axis = (0,40,0), shaftwidth = .5, color = color.blue)
wirelabel = label (pos = wire.pos + wire.axis, yoffset = 6, color = color.green, line = True, box = False,  text = 'Wire', opacity = 0)

# Draw the initial velocity at the initial position

startVel = arrow(pos = vector(pos[0][0], pos[0][1], pos[0][2]), axis = 3*vector(vel[0]), shaftwidth = .2, color = color.green)
label(pos = startVel.pos + vector(0,0,0), yoffset = 6, color = color.green, line = True, box = False,  text = 'Vo', opacity = 0)




# Draw the particle's path using the curve( ) object

path = curve( color = color.cyan, radius = 0.1)   # define the particle's path

n=0
while n < len(pos) - 1:
 #       rate(100)# this line slows down to 100 updates per second and allows to see the animation
        path.append( pos = vector(pos[n]) )  # add points to the curve
        n = n + 1



particle = sphere(pos = vector(pos[len(pos) - 1]), radius = 0.3, color = color.red)  #add the moving particle


