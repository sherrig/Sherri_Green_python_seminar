##Sherri Green
##Faster flux Homework 4
##3/2/15


#Faster way to find the flux is to use the rhs of Gauss's equation,
#and imagine a box around the ball. The flux through each of the sides
#of the box will be equal because of symmetry, so the flux through
#one side (the blanket), is just the total flux/6.

from visual import *
from const import E0

charge = 10.0e-6


#Visualization
blanketbox = box(pos = (0,0,0), length = 2, height = 2, width = 2, color = color.blue, opacity = .5)

chargedball = sphere(pos = (0,0,0), radius = .25, color = color.yellow)

arrow = arrow(pos=(0,0,0), axis = (0,0,1))


#flux calculation
flux = charge/(6*E0)

print "The flux through the blanket is", flux, "Nm^2/C"
