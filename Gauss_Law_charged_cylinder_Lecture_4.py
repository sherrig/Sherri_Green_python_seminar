#Gauss's law Lecture 3
#Sherri Green
#2/24/15

from math import *
from visual import *

e0=8.854187817*10**-12
lamda = 10**-5 #C/m
scalefactor = 1/(10**5)

print "Where do you want to calculate the elctric field?"
R = input("Enter R in m:")
Theta = input ("Enter the angle wrt the y-axis in radians:")
X = input ("Enter x, with x<<2, in m:")

P = [R, Theta, X]

#Calculate E-field vector
Emag = (lamda)/(2*pi*e0*P[0])

E = []   #(x,y,z)
E.append((Emag * P[2])/P[0])
E.append(Emag * cos(P[1]))
E.append(Emag * sin(P[1]))

print "E-field =",  E, "N/C"

#Calculate Flux

Flux = (lamda*4)/e0

print "Flux =", Flux, "C"

#Draw cylinder

rodcharge = cylinder (pos = (-4, 0,0), radius = .1, opacity = .5,
                      axis = (8,0,0), color = color.blue)
gaussian = cylinder (pos = (-2, 0,0), radius = P[0], opacity = .5,
                    axis = (4,0,0), color = color.white)
Efieldvector = arrow (pos = (P[2], P[0]*cos(P[1]), P[0]*sin(P[1])),
                      axis = (E[0]/200000, E[1]/200000, E[2]/200000),
                      color = color.green)
Evectorlabel = label (pos = Efieldvector.pos, text = 'Electric Field Vector')

xaxis = arrow (pos = (0,0,0), axis = (.5, 0,0), color = color.black)
yaxis = arrow (pos = (0,0,0), axis = (0, .5,0), color = color.black)
zaxis = arrow (pos = (0,0,0), axis = (0, 0,.5), color = color.black)

                                                    
                                
