#################################
# Title: Equipotentials symmetric               #            
# Filename: vp_lecture_6_sphere.py     #
# Original Author: Paola Rebusco#
# Most Recent Edit: 01/29/2015	#
# Last Editor: Paola Rebusco
# Visualization: Vpython
#################################

#Plot equipotential surfaces for a charged sphere. 
#Next to do:
#Plot equipotential surfaces for two point charges placed at random locations.

from visual import sphere,color,arrow,local_light,materials
from math import sqrt, pi,cos,sin
from const import E0

# E0 = 8.854187817e-12 If you are using glowscript you must define E0 and pi
# If you use glowscript you have to modify this code slightly:
# http://www.glowscript.org/docs/GlowScriptDocs/VPython-vs-GlowScript.html 

k = 1.0 / (4 * pi * E0)

lamp = local_light(pos=(30,30,40), color=color.yellow)

charge=sphere(pos=(0,0,0), radius=0.2,color=color.red,material=materials.shiny)

surface=range(10)

for j in surface:
    sphere(pos=(0,0,0), radius=0.4+0.1*j,color=color.yellow,opacity=0.05,material=materials.diffuse)
