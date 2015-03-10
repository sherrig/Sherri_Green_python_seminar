from math import sqrt, pi, exp
from const import E0
from matplotlib.pyplot import *
import numpy as np

k = 1.0 / (4*pi*E0)

def Phi(P):

    rodtop = np.array((0.0, 1.0, 0.0))
    rodbottom = np.array((0.0, 0.0, 0.0))
    rod = rodtop - rodbottom
    L = np.linalg.norm(rod)

    dy = 1.0e-3

    phi = 0.0

    for i in xrange(int(L/dy)):
        Pvec = np.array(P)
        pos_x = 0
        pos_y = rodbottom[1] + (rod[1]*i*dy)
        pos_z = 0
        pos = np.array(pos_x, pos_y, pos_z)
        lamda = 10.0e-8 * exp((-(pos_y - .5)**2)/.01)
        dq = lamda * dy
        rvec = P - pos
        r = np.linalg.norm(rvec)
        phi += (k * dq)/r

        return phi

V = []
path = range (50)
for step in path:
    V.append(Phi(.01, 0+step/20, 0 + step/30))

plot(path,V)
show()
