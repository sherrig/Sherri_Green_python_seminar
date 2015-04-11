#################################
# Title: B of a current-carrying ring #            
# Filename: vp_lecture_10.py     #
# Original Author: Paola Rebusco#
# Most Recent Edit: 02/23/2015	#
# Last Editor: Paola Rebusco
# Visualization: Vpython
#################################

# Visualize the different contributions to B, r hat, etc

from visual import ring,color, arrow, points,vector, cross, label,box
from math import sqrt, pi,cos,sin


#Draw a coordinate system
# Draw the (x,y,z) coordinate system - label (0,0,0)
a = 0.5                       #length of the (x,y,z) axis
arrow(pos = vector(0,0,0),axis = vector(a/2,0,0), shaftwidth = 0.01, color = color.white)
arrow(pos = vector(0,0,0),axis = vector(0,a/2,0), shaftwidth = 0.02, color = color.white)
arrow(pos = vector(0,0,0),axis = vector(0,0,a/2), shaftwidth = 0.02, color = color.white)
label(pos = vector(0,0,0), xoffset = -.5,yoffset = -0.5, zoffset = -.5,text='O',box = False,background = color.white,opacity = 0.06, line = False)
label(pos = vector(0+a/2,0,0), xoffset = -a/6,yoffset = +a/6, text = 'x',box = False,background = color.white,opacity = 0.06, line = False) 
label(pos = vector(0,a/2,0), xoffset = a/6,yoffset = a/10, text = 'y',box = False, background = color.white,opacity = 0.06, line = False) 
label(pos = vector(0,0,a/2), xoffset = -a/6,yoffset = a/6,zoffset = -a/6, text = 'z',box = False, background = color.white,opacity = 0.06, line = False) 



#Draw the ring

loop=ring(pos = (0,0,0), axis = (0,1,0), radius = 0.5, thickness = 0.02, color = color.yellow)

# Ask the user the location where we want to show the contributions to B

xp = input("Choose a point (enter x)")
yp = input("Choose a point (enter y)")
zp = input("Choose a point (enter z)")

P = (xp,yp,zp) # Location where we want to show the contributions to B

# Choose two infinitesimal points on the ring

sourceR = (0.5,0,0)
sourceL = (-0.5,0,0) 

# Show the two infinitesimal points (right and left)

pieceR = points(pos = sourceR, size = 10, color = color.red)
pieceL = points(pos = sourceL, size = 10, color = color.blue)


# Show the r hat vectors for the right and left infinitesimal pieces of ring at P

rhatR = arrow(pos = P, axis = (P[0]-sourceR[0],P[1]-sourceR[1],P[2]-sourceR[2]),\
              length=0.2, shaftwidth = 0.02, color = color.red)
rhatL = arrow(pos= P, axis = (P[0]-sourceL[0],P[1]-sourceL[1],P[2]-sourceL[2]), \
              length = 0.2 , shaftwidth = 0.02, color=color.blue)

# Decide the direction of the current dl (CCW from the top)-  at the location of the right infinitestimal
# it is dlR              

dlR = vector(0,0,-1)
RVec = vector(P[0]-sourceR[0],P[1]-sourceR[1],P[2]-sourceR[2])

# Use Biot-Savart to calculate the infinitesimal contribution to the magnetic field
# by one of the two infinitesimals             


dbR = arrow(pos= P, axis = cross(dlR,RVec), length = 0.2 , shaftwidth = 0.02, color = (1,0.7,0))


# Same calculation for the symmetric infinitesimal

dlL = vector(0,0,1)
LVec = vector(P[0]-sourceL[0],P[1]-sourceL[1],P[2]-sourceL[2])

dbL = arrow(pos = P, axis = cross(dlL,LVec),length = 0.2 , shaftwidth = 0.02, color = (0,0.7,1))

# Show the resulting unit vector for the magnetic field


result = arrow(pos = P, axis = cross(dlL,LVec) + cross(dlR,RVec), \
               length = 0.3 , shaftwidth = 0.02, color = (1,1,0))
