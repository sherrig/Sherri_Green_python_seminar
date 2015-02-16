#GlowScript 1.1 VPython

#################################
# Title: Homework 1 - VPython Script #
# Lesson: Drawing spheres and arrows #
# Filename: visual_pyhw_1_sol.py #
# Original Author: Analia Barrantes #
# Most Recent Edit: 1/23/2015 #
# Last Editor: Analia B #
#################################

# If you use Vpython instead of Glowscript  you have to modify this code slightly:
# http://www.glowscript.org/docs/GlowScriptDocs/VPython-vs-GlowScript.html

# Draw three spheres and connect them with arrows
from visual import *

# darw the 3 spheres
red_s=sphere(pos=vector(-1,0,0), radius=0.5,color=color.red)
blue_s =sphere(pos=vector(2,2,0), radius=0.5,color=color.blue)
green_s=sphere(pos=vector(2,-1,0), radius=0.5,color=color.green)

# Draw the vectors joining the 3 spheres

arrow(pos=red_s.pos,axis=blue_s.pos-red_s.pos)
arrow(pos=blue_s.pos,axis=red_s.pos-blue_s.pos)
arrow(pos=red_s.pos,axis=green_s.pos-red_s.pos)
arrow(pos=green_s.pos,axis=red_s.pos-green_s.pos)
arrow(pos=green_s.pos,axis=blue_s.pos-green_s.pos)
arrow(pos=blue_s.pos,axis=green_s.pos-blue_s.pos)
print("Position of red shere:", red_s.pos)
print("Position of blue shere:", blue_s.pos)
print("Position of green shere:", green_s.pos)
