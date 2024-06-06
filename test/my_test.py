import numpy as np
import matplotlib.pyplot as plt
from hhl_prototype import HHL

A = np.random.rand(4,4)
A = A+A.T

b = np.random.rand(4)

hhl = HHL()
circuit = hhl.construct_circuit(A, b)

circuit.draw('mpl')
plt.show()
