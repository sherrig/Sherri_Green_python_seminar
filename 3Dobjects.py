#Title: 3 Spheres and Arrows
# Filename: 3Dobjects.py
#Sherri Green
#2/8/15


#Draws 3 Spheres with Arrows attached in configuration from video
from visual import *

#Creates first ball
ball1 = sphere()
ball1.color = color.green
ball1.pos = (-1.5, 0, 0)
ball1.radius = .5

#Creates second ball
ball2 = sphere( radius = .5, pos = vector (0, 1, 0), color = color.green)

#Creates third ball
ball3 = sphere(radius =.5, pos = vector (0, -1, 0), color = color.green)

#Creates arrow for ball 1
vector1= arrow ()
vector1.color = color.red
vector1.pos = vector (-1.5, 0, 0)
vector1.axis = vector (0, -1, 0)

#Creates arrow for ball 2
vector2 = arrow (color = color.red, pos = (0,1,0), axis = vector(-1, 0, 0))
                 
#Creates arrow for ball 3
vector3 = arrow (color = color.red, pos = (0,-1,0), axis = vector (1, .9, -.2))
