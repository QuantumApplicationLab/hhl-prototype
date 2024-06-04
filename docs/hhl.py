import numpy as np
from hhl_prototype import HHL

A = np.random.rand(4,4)
A = A+A.T

b = np.random.rand(4)

hhl = HHL()
hhl.solve(A, b)