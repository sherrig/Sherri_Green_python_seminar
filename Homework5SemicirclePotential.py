##Sherri Green
##Homework 5
##3/8/15

#Calculate electric potential of charged semicircle at a generic point
#and then plots the potential as a function of distance along the linear
#path. Potential is zero at infinity.

import time
from const import E0
from math import cos, sin, pi, exp
import numpy as np
from matplotlib.pyplot import plot, show

k = 1.0 / (4*pi*E0)

def Phi(P):
    semicircle = (np.array([0, 0, 1.0]), np.array([0,0,0]))  #endpoints of semicircle
    theta_range = np.array([pi/2, -pi/2])
    theta_tot = theta_range[0]-theta_range[1]

    dtheta = 1.0e-3
    
    phi = 0.0

    for i in xrange (int(theta_tot/dtheta)):
        theta = theta_range[0] - i*dtheta                    #position of angle
        lamda = 10.0e-6/(1+ exp(-5*(theta-pi/2)))
        pos = np.array(semicircle[0]) + np.array([.5*cos(theta),       #position is top of semicircle plus conversion from polar -- have to subtract in z because it's going down from the top
                                                  0, -(.5+.5*sin(theta))])
        dq = lamda * .5 * dtheta
        r = np.linalg.norm(P-pos)
        phi += k * dq/r
        return phi    
        
path = range(50)
V =[]
for j in path:
    V.append(Phi([0+ j/50, .25 - j/100, 0 + j/100]))

plot (path, V)
show()

