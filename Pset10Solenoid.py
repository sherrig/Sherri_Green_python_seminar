##Sherri Green
##4/13/15
##Pset 10

##Calculate magnetic field everywhere in space produced by a current carrying solenoid of radius a, length L, and having N loops
##The magnetic field produced by a current carrying ring is basically the same as what we did in class

import numpy as np
from math import sin, cos, pi
from const import mu0
dtheta = 1e-4

I = 10.0
a = 0.5
L = 20.0
N = 100.0

def B(P,z):                                         #P is point where measuring B field, z is z location of center of ring
    B = np.array ((0.0, 0.0, 0.0))
    for i in xrange(int(2*pi/dtheta)):
           try:
               theta = i * dtheta
               pos = a * np.array((cos(theta),         # Location of differential current
                                sin(theta),
                                z))
               r = P - pos
               r_mag = np.linalg.norm(r)
               dl = a * dtheta * np.array((-sin(theta),# Differential wire vector, a positive current flows CCW from the top
                                        cos(theta),
                                        0.0))
               dB = (mu0 * I * np.cross(dl, r) /       # Invoke Biot-Savart Law
                  (4.0 * pi * r_mag**3))
               B = B + dB
           except KeyboardInterrupt:                   
               print 'theta =', i * dtheta, "z =", z            
               prompt = 'Continue execution? (Y/N) '
               persevere = raw_input(prompt)
               if not persevere.lower()[0] == 'y':
                    msg = 'Iteration Limit Exceeded'
                    raise Exception(msg)
    return B

def B_sol(P):
    B_sol = np.array((0.0, 0.0, 0.0))
    for i in xrange(int(N)):
        try:
            z = (L/(N-1.0))*i
            B_sol = B_sol + B(P,z)
        except KeyboardInterrupt:
            print "N =", i
            prompt = 'Continute execution? (Y/N)'
            persevere = raw_input(prompt)
            if not persevere.lower()[0] == 'y':
                msg = "Too many coils"
                raise Exception(msg)

    return B_sol
