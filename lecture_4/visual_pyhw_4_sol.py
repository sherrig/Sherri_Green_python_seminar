#################################
# Title: Homework 4 - VPython Script #
# Lesson: Charged blanket #
# Filename: visual_pyhw_4_sol.py #
# Original Author: Paola Rebusco #
# Most Recent Edit: 1/27/2015 #
# Last Editor: PR #
#################################

# Calculate the flux of a point charge through the face of a cube (see homework 4)
from visual import box,sphere,color

from math import sqrt, pi,cos,sin
from const import E0

# E0 = 8.854187817e-12 If you are using glowscript you must define E0 and pi
# If you use glowscript you have to modify this code slightly:
# http://www.glowscript.org/docs/GlowScriptDocs/VPython-vs-GlowScript.html 



# draw the point charge
charge=sphere(pos=(0,0,0), radius=0.1,color=color.red)


#draw a gaussian surface that enclosed the charge\

gauss=box(pos=(0,0,0),length=2,width=2,height=2,color=color.green,opacity=0.5)

q=1

totflux= q/E0 

print "The flux through one of the faces is: " , totflux/6, " N m2**/C"
