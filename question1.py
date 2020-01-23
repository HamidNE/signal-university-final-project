import numpy as np
from numpy import sqrt
import matplotlib.pyplot as plt
import scipy as sp
import math


def sinyal(N, c, f, p):
    y = np.zeros(N)
    t = np.linspace(0, 2*np.pi, N)
    Nf = len(c)
    for i in range(Nf):
        y += c[i]*np.sin(f[i]*t)
    return y


 # Signal Generator
c = [2, 5, 10]
f = [50, 150, 300]
p = [0, 0]
N = 2000
x = np.linspace(0, 2.0*math.pi, N)
y = sinyal(N, c, f, p)
plt.plot(x[:100], y[:100])
plt.show()
