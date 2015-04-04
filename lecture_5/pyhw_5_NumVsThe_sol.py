# Title: Py Homework 5 Solution #
# Lesson: Electric Potential #
# Filename: pyhw_5_sol.py #
# Original Author: Joe Griffin #
# Most Recent Edit: 1/22/2015 #
# Last Editor: Joe Griffin #
#################################



# 1. We will calculate the potential due to a charged semicircle along a line
# 2. We will compare the numerical calculation, Vnum, and the theretical result, Vthe,
# of the potential at points on the axis passing through the center of the semicircle and
# perpendicular to the plane in which the semicircle is contained
# 3. We will calculate the absolute value of the relative error err=|(Vnum-Vthe)/Vthe|
# 4. Plot the potential along the line

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
from math import sqrt, pi, exp, sin, cos,log
from const import E0
k = 1.0 / (4 * pi * E0)

# In the repository I was using without pi/2

def lamda(theta):
	return 1e-6 / (1 + exp(-5 * (theta - pi/2)) )

def Phi(P):
		Q = (np.array([0, 0, 0]), # (End 1, middle, end 2)
		np.array([0.5, 0, 0.5]),
		np.array([0, 0, 1])
		)
		R = np.linalg.norm(Q[2] - Q[0]) / 2
		ctr = (Q[0] + Q[2]) / 2.0
		end = (Q[2] - ctr) / R # Direction across semicircle
		perp = (Q[1] - ctr) / R # Direction into semicircle

		dtheta = 1.0e-3 # Integral increment angle (precision)

		phi = 0.0 # Electrostatic Potential

		for i in xrange(int(pi / dtheta)): # Create our integration iterable
				theta = (i * dtheta) - (pi / 2)
				dq = lamda(theta) * R * dtheta
				ends = sin(theta) * end * R
				perps = cos(theta) * perp * R
				pos = ctr +ends + perps
				r = np.linalg.norm(P - pos)
				phi += k * dq / r
		return phi

#Calculate the analytical expression of the electric potential only along the y-axis

def Phith(yp):
		Q = (np.array([0, 0, 0]), # (End 1, middle, end 2)
		np.array([0.5, 0, 0.5]),
		np.array([0, 0, 1])
		)
		R = np.linalg.norm(Q[2] - Q[0]) / 2
		r = sqrt( R**2 + yp**2)
		factor = pi+ (1./5.)*log( 2. / (1 + exp(5*pi) ) )
		Phith = k * R * (1e-6) * factor /r
		return Phith

#Will calculate the numerical and the theoretical potential along the y-axis

path = range(50)

V = [] #numerical
Vth=[] #theoretical
err=[] #absolute value of the relative error

for j in path:
		P = np.array([0., j / 25.0, 0.5])
		V.append(Phi(P))
		Vth.append(Phith(P[1]))

for j in path:
		err.append(abs((V[j]-Vth[j])/Vth[j]))

# Calculate the maximum of the magnitude of the error

ma=max(err)
print 'Maximum value of the relative error=', ma

# Plot the results
# Plot the electric potential in the upper half of the window

plt.subplot(211)
plt.plot(path,V)
plt.grid(True)
plt.title('Potential due to a non-uniformly charged semicircle')
plt.xlabel(' step number')
plt.ylabel(' V (V) electric potential')
# Plot the absolute value of the relative error in the lower half of the window
plt.subplot(212)
plt.plot(path,err,'r--')
plt.grid(True)
plt.xlabel(' step number')
plt.ylabel(' |Vnum-Vthe/Vthe|')
plt.show()
