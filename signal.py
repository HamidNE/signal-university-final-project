import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-0.02, 0.05, 1000)
plt.plot(t, 325 * np.sin(2*np.pi*50*t))
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title(r'Plot of CT signal $x(t)=325 \sin(2\pi 50 t)$')
plt.xlim([-0.02, 0.05])
plt.show()
