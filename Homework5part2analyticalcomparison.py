##Sherri Green
##Homework 5 Part 2
##3/8/15

#Compare analytical and computational values for potential. Potential is zero at infinity.

import time
from const import E0
from math import cos, sin, pi, exp, sqrt, log
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
        theta = theta_range[0] + i*dtheta                    #position of angle
        lamda = 10.0e-6/(1+ exp(-5*(theta-pi/2)))
        pos = np.array(semicircle[0]) + np.array([.5*cos(theta),       #position is top of semicircle plus conversion from polar -- have to subtract in z because it's going down from the top
                                                  0, -(.5+.5*sin(theta))])
        dq = lamda * .5 * dtheta
        r = np.linalg.norm(P-pos)
        phi += k * dq/r
        return phi

#Analytical potential function
def Phi_an(P):
    def integrated_potential (theta):
        value = (1/5)*(log(exp(5*theta)+exp(5*pi/2)))
        return value
        
    phi_an = (((k*10.0e-6*.5)/(sqrt(.5**2 + P[1]**2)))
              * (integrated_potential(pi/2)
                 - integrated_potential(-pi/2)))
    return phi_an

Vnum = []
Vth = []
err = []
        
path = range(200)

for j in path:
    Vnum.append(Phi([0, 0 + j/100, 0]))
    Vth.append(Phi_an([0, 0 + j/100, 0]))
    err.append(abs((Vnum[j]-Vth[j])/Vth[j]))

#Calculate max magnitude of error

ma = max(err)
print 'Maximum value of the relative error =', ma

#Graph Vnum vs y and Vth vs y

plot(path, Vnum)
plot (path, Vth)
show()
