import matplotlib.pyplot as plt
from math import sqrt
import numpy as np
x = [1, 2, 3, 4, 5]
y = [1., 0.25, 1./9, 1./16, 1./25]
plt.plot(x, y)
plt.show()






















v = [1, 3, 5]
mag = sqrt((v[0]**2) + (v[1]**2) + (v[2]**2))
vec = np.array(v)
npmag = np.linalg.norm(vec)
