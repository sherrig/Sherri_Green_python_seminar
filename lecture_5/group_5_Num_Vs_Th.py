#################################
# Title: Lecture 5 Group Script #
# Lesson: Electric Potential #
# Filename: group_5.py #
# Original Author: Joe Griffin #
# Most Recent Edit: 1/23/2015 #
# Last Editor: AB #
#################################


# With this script we will be able to:
# Calculate the potential due to a uniformly charged rod at a point in space. (Vnumerical)
# Plot the potential along the segment joining the two points: (1, 2, 2) and (1.5, 0.5, 1) 
# Evaluate the theoretical expression of the potential obtained by analytical integration (Vtheoretical)
# Calculate and plot along the same segment the magnitude of the relative error  defined as:
# error= |(Vnumerical - Vtheoretical/Vtheoretical|

import matplotlib.pyplot as plt
from math import sqrt, pi, log
from const import E0
from matplotlib.pyplot import *
k = 1.0 / (4 * pi * E0)

# Function: Numerical potential at a given point in space
def Phi(P):
    lamda = 3e-5
    rod = ((0.0, 0.0, 0.0), (0.0, 1.0, 0.0)) # Endpoint 1, endpoint 2
    L = sqrt(((rod[1][0] - rod[0][0])**2) + # Length of rod
        	((rod[1][1] - rod[0][1])**2) +
        	((rod[1][2] - rod[0][2])**2)
        	)
    rod_x = (rod[1][0] - rod[0][0]) / L # x, y, z components of rod vector
    rod_y = (rod[1][1] - rod[0][1]) / L
    rod_z = (rod[1][2] - rod[0][2]) / L
    dy = 1.0e-4 # Integral increment length (precision)
    phi = 0.0 # Electrostatic Potential
    for i in xrange(int(L / dy)): # Create our integration iterable
        dq = lamda * dy
        pos_x = 0				 # Pos is location in space of dq
        pos_y = rod[0][1] + (rod_y * i * dy)
        pos_z = 0
        r = sqrt(((P[0] - pos_x)**2) +               # r is distance from pos to P
                ((P[1] - pos_y)**2) +
                ((P[2] - pos_z)**2)
                )
        phi += k * dq / r
    return phi

# Function: Theoretical potential at a given point in space

def Phi_th(P):
    lamda = 3e-5
    rod = ((0.0, 0.0, 0.0), (0.0, 1.0, 0.0)) # Endpoint 1, endpoint 2
    L = sqrt(((rod[1][0] - rod[0][0])**2) + # Length of rod
        ((rod[1][1] - rod[0][1])**2) +
        ((rod[1][2] - rod[0][2])**2)
        )
    
    num = P[1]-L + sqrt(P[0]**2+(P[1]-L)**2+P[2]**2)
    den = P[1] + sqrt(P[0]**2 + P[1]**2+P[2]**2)
    phi=-k*lamda*log(num/den)
    return phi



# Initialize the variables

V= []                 # numerical potential
V1 = []               # theoretical potential
err=[]                # magnitude of the relative error

# Calculate the potentials and the magnitude of the relative error 
# along the line joining the points  (1, 2, 2) and (1.5, 0.5, 1)
# 

path=range(500)	         # Number of points along the path

for step in path:		
    V.append(Phi((1 - (step / 1e3),
             	  2 - (3 * (step / 1e3)),
                  2 - (3 * (step / 500.0))
                  )))
    V1.append(Phi_th((1 - (step / 1e3),
            	      2 - (3 * (step / 1e3)),
                      2 - (3 * (step / 500.0))
                     )))
    err.append(abs((V[step]-V1[step])/V1[step]))
	
# Calculate the maximum  of the magnitude of the error

ma=max(err)
print 'Maximum value of the relative error=', ma

# Plot the results

plt.figure(1) 

# Plot the electric potential in the upper half of the window
plt.subplot(211)
plt.plot(path,V)
plt.grid(True)
plt.title('Potential due to a uniformly charged rod')
plt.xlabel(' step number')
plt.ylabel(' V (V)')

# Plot the error in the lower half of the window

plt.subplot(212)
plt.plot(path,err,'r--')
plt.grid(True)
plt.xlabel(' step number')
plt.ylabel('  |Vnum-Vthe/Vthe|')

plt.show()


