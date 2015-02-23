#Draw E-field for dipole at 5 points
#Sherri Green
#2/22/15

from math import sqrt
from visual import *

#Draw charges

q1 = sphere (radius = .25, pos = (0,.5,0), color = color.green)
q2 = sphere (radius = .25, pos = (0, -.5, 0), color = color.green)

#Draw E-field vectors

v1 = arrow (pos = (.5, 0, 0), axis = (0, -2*sqrt(2), 0), color = color.blue)
v2 = arrow (pos = (-.5, 0,0), axis = (0, -2*sqrt(2), 0), color = color.blue)
v3 = arrow (pos = (0,0,.5), axis = (0, -2*sqrt(2), 0), color = color.red)
v4 = arrow (pos = (0,0,-.5), axis = (0, -2*sqrt(2), 0), color = color.red)
v5 = arrow (pos = (0,0,0), axis = (0,-8,0), color = color.magenta, shaftwidth = .2, opacity = .7)

#print E-fields

print "E-field at ", v1.pos, "is", v1.axis, "N/C"
print "E-field at ", v2.pos, "is", v2.axis, "N/C"
print "E-field at ", v3.pos, "is", v3.axis, "N/C"
print "E-field at ", v4.pos, "is", v4.axis, "N/C"
print "E-field at ", v5.pos, "is", v5.axis, "N/C"

# Code works as expected. Pass.
