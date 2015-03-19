##Sherri Green
##Homework 5 Part 2
##3/8/15

#Compare analytical and computational values for potential. Potential is zero at infinity.

import time
from const import E0
from math import cos, sin, pi, exp, sqrt, log, atan
import numpy as np
from matplotlib.pyplot import plot, show

k = 1.0 / (4*pi*E0)

#computational potential function
def Phi(P):
    semicircle = (np.array([0, 0, 1.0]), np.array([0,0,0]))  #endpoints of semicircle
    theta_range = np.array([pi/2, -pi/2])
    theta_tot = theta_range[0]-theta_range[1]

    dtheta = 1.0e-3
    
    phi = 0.0

    for i in xrange (int(theta_tot/dtheta)):
        theta = theta_range[1] + i*dtheta                    #position of angle
        lamda = (1e-6)/(1+ exp(-5*(theta-(pi/2))))
        pos = np.array(semicircle[0] + np.array([.5*cos(theta),       #position is top of semicircle plus conversion from polar
                                                  0, (.5 + .5*sin(theta))]))
        dq = lamda * .5 * dtheta
        r = np.linalg.norm(P-pos)
        phi += k * dq/r
    return phi
    
#Analytical potential function
def Phi_an(P):
    phi_an = abs(((pi + (1/5)*(log(2/(1+exp(5*pi)))))* k *
              10.0e-6 * (atan(P[1]) - pi/2)))  #### Uhm...double check!
    return phi_an

    
Vnum = []
Vth = []
err = []
        
path = range(200)

for j in path:
    Vnum.append(Phi([0, 0 + j/100.0, 0.5]))
    Vth.append(Phi_an([0, 0 + j/100.0, 0.5]))
    err.append(abs((Vnum[j]-Vth[j])/Vth[j]))

#Calculate max magnitude of error

ma = max(err)
print 'Maximum value of the relative error =', ma

#Graph Vnum vs y and Vth vs y

plot(path, Vnum)
plot (path, Vth)
show()

#Changing dtheta doesn't seem to change my error, but error also seems to be pretty large, so maybe one of my voltages are wrong.
