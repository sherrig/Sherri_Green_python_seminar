

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

wire = shapes.line(start = (0,-1e4,0), end = (0, 1e4, 0))

# 1. Draw a reference xz-plane with the size determined by the diameter of the helix

pos_a = np.array(pos)                  #convert the position list to a numpy array
xmax, ymax, zmax = pos_a.max(axis = 0)     # to use numpy max and min functions to find 
xmin, ymin, zmin = pos_a.min(axis = 0)     # the corners of the box 

center = vector((xmax + xmin) / 2., pos[0][1] , (zmax + zmin) / 2.)   #center of the helix

box(pos = center, length = 2 * (xmax - xmin), width = 2 * (zmax - zmin),
    height = 0.05, color = color.blue, opacity = 0.2)




# 2. Draw the (x,y,z) - at the center of the helix

l = [xmax - xmin, zmax - zmin]       # length introduced to scale vectors

print "max", xmax, ymax, zmax
print "min", xmin, ymin, zmin
print "center", center
print "initial postion", pos[0]

# Draw the  Magnetic field  at the center of the helice

if ymax < xmax:
    b = max(l)
if ymax > xmax:
    b = ymax

B = arrow(pos = center + vector(0, -b / 2, 0), axis = vector(0, b, 0), shaftwidth = 0.2,
          headwidth = .8, color = color.blue, opacity = 0.7)
label(pos = center + vector(0, b / 2, 0), opacity = 0, color = color.blue, height = 16, xoffset = 4, line = False, box = False,  text = 'B')

# If you want a bunch of B-field vectors inside the helix try this:

#j = mag(center) / 3
#for i in range(9):    # 9 vectors in a circle at 1/3 from the center of the helix
#    r_B = vector(j * cos(i * pi/4), -b/2, j * sin(i * pi/4)) + center  #points in a circle of radius 1 centered at the center of the helix
#    arrow(pos = r_B, axis = vector(0,b/2,0), shaftwidth = 0.2, color = color.blue, opacity = 0.7)     #unit vectors


# Draw the initial velocity at the initial position

startVel = arrow(pos = vector(pos[0][0], pos[0][1], pos[0][2]), axis = vector(vel[0]), shaftwidth = .3, color = color.green)
label(pos = startVel.pos + vector(0,0,0), yoffset = 6, color = color.green, line = True, box = False,  text = 'Vo', opacity = 0)



#### You want to do this
# Draw the particle's path using the curve( ) object

path = curve( color = color.cyan, radius = 0.1)   # define the particle's path

n=0
while n < len(pos) - 1:
 #       rate(100)# this line slows down to 100 updates per second and allows to see the animation
        path.append( pos = vector(pos[n]) )  # add points to the curve
        n = n + 1



particle = sphere(pos = vector(pos[len(pos) - 1]), radius = 0.3, color = color.red)  #add the moving particle


