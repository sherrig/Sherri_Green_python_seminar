#################################
# Title: Equipotentials               #            
# Filename: vp_lecture_6_2_points.py     #
# Original Author: Paola Rebusco#
# Most Recent Edit: 02/26/2015	#
# Last Editor: Paola Rebusco
# Visualization: Vpython
#################################


#Plot equipotential surfaces for two point charges placed at random locations on a plane.
# Explanation+script from: http://chuck.emich.edu/dpawlows/includes/350/2dplotting.pdf

import numpy as np
from matplotlib import pyplot as p
K = 9.0e9

q = [None, None]

# Charges are represented as [x, y, z, q], length in m, q in Coulomb

q[0] = [0.02, 0, 0, 1e3] 
q[1] = [-0.02, 0, 0, -3e3]


#def potential(xl, yl, charges):
#    phi = 0.
#    for i in xrange(len(charges)):
#
#            dx = xl - charges[i][0]
#            dy = yl - charges[i][1]
#            r = np.sqrt(dx*dx + dy*dy)
#
#            phi += K*charges[i][3]/r
#
#    return phi

#Make a grid

x = np.arange(-.051,.05,.002)
y = np.arange(-.051,.05,.002)


#contour wants the x and y values to be defined at every point
#on the grid.

X, Y = np.meshgrid(x,y)

r1 = np.sqrt((X-q[0][0])**2+(Y-q[0][1])**2)
r2 = np.sqrt((X-q[1][0])**2+(Y-q[1][1])**2)

# define the equipotentials

Z = K * q[0][3]/ r1 + K * q[1][3]/ r2

# 
#for item in xrange(len(x)):
#     Z.append(potential(x[item],y[item],q))
#


#plot it

cont = p.contourf(X,Y,Z,100)
p.title('Potential due to two point charges')
p.xlabel('x (m)')
p.ylabel('y (m)')

cb = p.colorbar(cont)
cb.set_label('Potential (V)')

p.show()
p.savefig('point_c_equipot.ps')

