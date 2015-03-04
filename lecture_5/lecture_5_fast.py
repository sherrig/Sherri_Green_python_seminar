#################################
# Title: Lecture 5              #
# Lesson: Electric Potential    #
# Filename: lecture_5.py	#
# Original Author: Joe Griffin	#
# Most Recent Edit: 1/15/2015	#
# Last Editor: Joe Griffin	#
#################################

# Relevant Classes: 6.004

# We will calculate the potential due to a charged rod along a line, then graph that potential
#   curve as a function of position.

import time
import numpy as np
from matplotlib.pyplot import plot, show
from math import sqrt, pi, exp
from const import E0

k = 1.0 / (4 * pi * E0)


def lamda(d):
    return exp(-((d - 0.5)**2) / 0.01) * 1e-8

def Phi(Point):
    rod = (np.array([0.0, 0.0, 0.0]),                   # Endpoint 1, endpoint 2
           np.array([0.0, 1.0, 0.0])
           )
    
    rod_vec = rod[1] - rod[0]
    L = np.linalg.norm(rod_vec)                         # np.linalg.norm() calculates vector
                                                        #   magnitude, which is handy here
    
    rod_dir = rod_vec / L                               # rod direction vector
    dy = 1.0e-4                                         # Integral increment length (precision)

    i = np.arange(int(L / dy), dtype = np.float64)      # Create our integration iterable
    l_fast = np.vectorize(lamda, otypes = [np.float64])
    dq = l_fast(dy * i) * dy
    p = ((np.outer(np.ones((int(L / dy), 1)), rod[0])) +# p is location in space of dq
         (np.outer(i, rod_vec) * dy)
         )
    P = np.outer(np.ones((int(L / dy), 1)), Point)
    r = np.linalg.norm(P - p, axis = 1)
    phi = k * np.sum(np.divide(dq, r))                  # Integral is "infinite" sum of dPhi's
    return phi

start = time.time()
path = range(50)
V = []
for j in path:
    V.append(Phi(np.array([0.01, j / 20.0, j / 30.0])))

plot(path, V)
print start - time.time()
show()
