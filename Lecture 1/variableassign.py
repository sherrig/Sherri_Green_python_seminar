#Title: Variable Assignment
#Filename: variableassign.py
#Sherri Green
#2/8/15

#Draws 3 spheres connected ccw by arrows

from visual import *

#Draw spheres

ball1 = sphere(color = color.green, pos = (1, 2, 0), radius = .5)
ball2 = sphere(color = ball1.color, pos = (1, -2, 0), radius = .5)
ball3 = sphere(color = ball1.color, pos = (-2, 0, 0), radius = .5)

#Draw arrows

arrow1 = arrow(color = color.red, pos = ball1.pos, axis = ball3.pos-ball1.pos)
arrow2 = arrow (color = color.red, pos = ball3.pos, axis = ball2.pos-ball3.pos)
arrow3 = arrow(color = color.red, pos = ball2.pos, axis = ball1.pos-ball2.pos)
