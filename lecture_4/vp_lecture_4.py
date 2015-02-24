# -*- coding: utf-8 -*-
#################################
# Title: Gauss rod #
# Filename: vp_lecture_4.py #
# Original Author: Paola Rebusco#
# Most Recent Edit: 01/29/2015 #
# Last Editor: AB            #
# VPython Version            #
#################################

#A thin rod of length L = 8 m is charged uniformly with a charge density
#per unit length given by  λ0 = 10-5C/m. The rod is oriented along the x-axis
# centered at the origin.
# Calculate and visualize E and the Gaussian surface.


from __future__ import division
from visual import *
from math import sqrt, pi,cos,sin
from const import E0

# E0 = 8.854187817e-12 If you are using glowscript you must define E0 and pi
# If you use glowscript you have to modify this code slightly:
# http://www.glowscript.org/docs/GlowScriptDocs/VPython-vs-GlowScript.html

k = 1.0 / (4 * pi * E0)

# ask for the location where to calculate E
print "Where do you want to calculate the electric field?"
R= input(" Enter R in m: ")

theta= input(" Enter theta in deg: ")
theta=theta*pi/180.    #convert deg to rad

x= input(" Enter x, with |x|<<2 m : ")

# Draw the rod centered at (0,0,0)
L=8.                          #length of the rod
rod = cylinder(pos=(-L/2,0,0), axis=(L,0,0), radius=0.03,
               opacity=0.5,color=color.red)

# Draw the Gaussian cylinder of radius = R
length =L/2                        #length of the gaussian cylinder 
gauss = cylinder(pos=(-length/2,0,0), axis=(length,0,0), radius=R,color=color.white,opacity=0.3)



#Calculate the charge enclosed 
density=1.0e-5                       #charge per unit length [C/m]
charge = density * length            # charge enclosed by the gaussian cylinder
cylinder_area = 2 * pi * R * length
Emagn = charge / (E0 * cylinder_area)# Calculate the magnitude of the electric field vector

# Write the E field vector in cartesian coordinates: (Ex, Ey, Ez)

z= R * sin(theta) # z coordinate of the location where we calculate E
y= R * cos(theta) # y coordinate of the location where we calculate E

# Draw the E field vector at the given point and label it with the letter E
E_field= (0,Emagn*y/R,Emagn*z/R)
scale=1./(Emagn)                # scale to adjust the length of the arrow representing E
E_field= (0,scale*Emagn*y/R,scale*Emagn*z/R) # in Vpython scalar*vector is wrong - must multiply inside  

#E_vec = arrow(pos=(x,y,z), axis=E_field, shaftwidth=0.08, color=color.green)
#label(pos=vector(x,y,z),xoffset=8, yoffset=10, text='E',box=false,line=false)
#curve(pos=[vector(x,0,0), vector(x,y,z)], color=color.white,radius=0.006)     #this line is to show the radius of
                                                                           # the Gaussian surface at the point 
                                                                           # where the E-fiels is calculated

# Calculate the total flux
flux = Emagn * cylinder_area

# Draw the (x,y,z) coordinate system center at the center of the rod - label (0,0,0)
a=1.                       #length of the (x,y,z) axis
arrow(pos=vector(0,0,0),axis=vector(a/2,0,0), shaftwidth=0.04, color=color.white)
arrow(pos=vector(0,0,0),axis=vector(0,a/2,0), shaftwidth=0.04, color=color.white)
arrow(pos=vector(0,0,0),axis=vector(0,0,a/2), shaftwidth=0.04, color=color.white)

label(pos=vector(0,0,0), xoffset=-.5,yoffset=-0.5, zoffset=-.5,text='O',
      box=false,background=color.white,opacity=0.06, line=false)
label(pos=vector(a/2,0,0), xoffset=-a/6,yoffset=+a/6, text='x',
      box=false,background=color.white,opacity=0.06, line=false) 
label(pos=vector(0,a/2,0), xoffset=a/6,yoffset=a/10, text='y',
      box=false, background=color.white,opacity=0.06, line= false) 
label(pos=vector(0,0,a/2), xoffset=-a/6,yoffset=a/6,zoffset=-a/6, text='z',
      box=false, background=color.white,opacity=0.06, line= false) 


#Print the results
print'P = (R,theta,x) = ', info
print 'Magnitude of the Efield =', mag(E_field), '[N/C]'
print 'Electric flux = ', flux, '[Nm^2/C]'


# Extra work - not requested
# Draw an arclength measured from +y-axis to indicate the angle theta
curve(pos=[vector(x,0,0), vector(x,R/2,0)], color=color.white,radius=0.006) # reference axis parallel to y, passing 
                                                                            # throuh x
dtheta=1e-3
for j in range(int(theta/dtheta)):
    s1=vector(x, R/4*cos(j*dtheta),R/4*sin(j*dtheta) )
    s2=vector(x, R/4*cos((j+1)*dtheta),R/4*sin((j+1)*dtheta) )
    curve(pos=[s1,s2],radius=0.005,color=color.white)


