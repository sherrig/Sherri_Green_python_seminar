GlowScript 1.1 VPython

#################################
# Title: Homework 2 - VPython Script #
# Lesson: Elecric Fields #
# Filename: visual_pyhw_2.py #
# Original Author: Analia Barrantes #
# Most Recent Edit: 1/22/2015 #
# Last Editor: Analia B #
#################################


# Draw the E-field vectors due to a dipole at 5 locations
# by adding the E-field due to the positive and the negative charge.
# We will use the function done in part a of the homework pyhw_2_sol.py

# If you use Vpython instead of Glowscript  you have to modify this code slightly:
# http://www.glowscript.org/docs/GlowScriptDocs/VPython-vs-GlowScript.html


from __future__ import division
from visual import *

E0 = 8.854187817e-12  # units: C^2/(N*m^2)
k = 1.0 / (4 * pi * E0)


q_mag=4 * pi * E0                       # magnitude of the charge of the dipole in C
a=0.5                                   # 2a is the charge separation
r_p=vector(0,a,0)                       #position of the positive charge
r_n=vector(0,-a,0)                      # position of the negative charge




# draw the positive (red) and the negative (blue) charges

charge_p=sphere(pos=r_p, radius=0.05,color=color.red)  
charge_n=sphere(pos=r_n, radius=0.05,color=color.blue)  

#Define the input to the E(q,P) function

qp=[r_p.x,r_p.y,r_p.z,q_mag]      # point source - positive charge
qn=[r_n.x,r_n.y,r_n.z,-q_mag]     # point source - negative charge

def E(q, P):
    r = (P[0] - q[0], P[1] - q[1], P[2] - q[2])     # (point field - point source)
    mag = sqrt((r[0]**2) + (r[1]**2) + (r[2]**2))
    field = []
    field.append(k * (r[0] / mag) * (q[3] / (mag**2))) # Calculate x, y, and z components
    field.append(k * (r[1] / mag) * (q[3] / (mag**2)))
    field.append(k * (r[2] / mag) * (q[3] / (mag**2)))
    return field
 
scale=0.1                         # scale factor for the E-filed arrows

# drawing the E-field vectors at the five different points 

#at the origin
P=[0,0,0]
Ep=E(qp,P)                                              # E - field due to the positive charge
En=E(qn,P)                                              # E - field due to the negative charge
Etot_vec=vector(Ep[0]+En[0],Ep[1]+En[1],Ep[2]+En[2])       # Define the total field vector 
arrow(pos=vector(P[0],P[1],P[2]),axis=scale*(Etot_vec),shaftwidth=0.03,headwidth=3*0.03)
print("at (  0,0,0) vector E=", Etot_vec, "[V/m]")

# at the +x-axis
P=[a,0,0]
Ep=E(qp,P)                                              # E - field due to the positive charge
En=E(qn,P)                                              # E - field due to the negative charge
Etot_vec=vector(Ep[0]+En[0],Ep[1]+En[1],Ep[2]+En[2])       # Define the total field vector 
arrow(pos=vector(P[0],P[1],P[2]),axis=scale*(Etot_vec),shaftwidth=0.03,headwidth=3*0.03,color=color.red)
print("at (  a,0,0) vector E=", Etot_vec, "[V/m]")


# at the -z-axis
P=[0,0,-a]
Ep=E(qp,P)                                              # E - field due to the positive charge
En=E(qn,P)                                              # E - field due to the negative charge
Etot_vec=vector(Ep[0]+En[0],Ep[1]+En[1],Ep[2]+En[2])       # Define the total field vector 
arrow(pos=vector(P[0],P[1],P[2]),axis=scale*(Etot_vec),shaftwidth=0.03,headwidth=3*0.03,color=color.green)
print("at ( 0,0,-a) vector E=", Etot_vec, "[V/m]")


# At the -x-axis
P=[-a,0,0]
Ep=E(qp,P)                                              # E - field due to the positive charge
En=E(qn,P)                                              # E - field due to the negative charge
Etot_vec=vector(Ep[0]+En[0],Ep[1]+En[1],Ep[2]+En[2])       # Define the total field vector 
arrow(pos=vector(P[0],P[1],P[2]),axis=scale*(Etot_vec),shaftwidth=0.03,headwidth=3*0.03,color=color.orange)
print("at ( -a,0,0) vector E=", Etot_vec, "[V/m]")

# At the +z-axis
P=[0,0,a]
Ep=E(qp,P)                                              # E - field due to the positive charge
En=E(qn,P)                                              # E - field due to the negative charge
Etot_vec=vector(Ep[0]+En[0],Ep[1]+En[1],Ep[2]+En[2])       # Define the total field vector 
arrow(pos=vector(P[0],P[1],P[2]),axis=scale*(Etot_vec),shaftwidth=0.03,headwidth=3*0.03,color=color.yellow,opacity=0.5)
print("at ( 0,0,a) vector E=", Etot_vec, "[V/m]")
