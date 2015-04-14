a = range(10)
a[len(a) - 2] = a[len(a) - 2] + 1
a[-2] += 1
b = a[0:len(a)]
b = a[:]
import numpy
import matplotlib
import numpy as np, matplotlib.pyplot as plt

L = []
for i in range(3):
    L.append(i**2)

L = [i**2 for i in range(3)]

D = {i**2: i**3 for i in range(3)}

def ll(resistances):
    inverse = 0.0
    for i in xrange(len(resistances)):
        inverse = inverse + (1.0 / resistances[i])
    return 1.0 / inverse

def ll(*res): return 1.0 / sum([(1.0 / i) for i in res])

ll(1, 2)

def B_ring(P, on_axis = True):
    if on_axis: return analytical_B(P[0])
    else: return Bnp(P)

B_ring(np.array((1, 2, 3)), on_axis = False)

def dict_reader(**kwargs): return kwargs
