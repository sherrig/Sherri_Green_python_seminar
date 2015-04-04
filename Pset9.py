#Sherri Green
#4/4/15
#Pset 9
#Calculates velocity and position of proton based on forces caused by an infinite wire along the y-axis with a current and charge density

import numpy as np
from const import mu0, E0
from math import pi
import matplotlib.pyplot as plt
dt = 1e-3                                           # Simulator Settings
numPoints = 100

m = 1e-22                                           # Particle Properties
q = 1.6e-19
lamda = 1e-15 #C/m
I = 1e-4 #Amps

startPos = np.array((1.0, 2.0, 1.0))                # Initial Conditions
startVel = np.array((5.0,5.0, 5.0))

time = []
position = []

with open('traj.txt', 'w', 0) as text:              # Open a writeable text file
    p = startPos                                    # Copy/paste w/o `with` then indent & add file I/O
    v = startVel
    for iteration in xrange(int(numPoints)):
        t = dt * iteration
        B = (((mu0*I)/(2*pi*(p[0]**2+p[2]**2)))*   #B field should be perpendicular to r, so its direction is z i hat -x k hat but normalized (I think)
             np.array((p[2], 0, -p[0])))
        E = ((lamda/(2*pi*E0*(p[0]**2+p[2]**2)))*
             np.array((p[0], 0, p[2])))
        f = q*E + np.cross(q * v, B)                      # Lorenz force calculation
        a = f / m                                   
        v = v + a * dt                              # Integrals
        p = p + v * dt
        pVec = p.tolist()
        position.append(pVec)
        vVec = v.tolist()                           
        aVec = a.tolist()
        time.append(t)
        text.write(str((pVec, vVec, aVec)) + '\n')  # Data dump



plt.plot(time, position)
plt.show
