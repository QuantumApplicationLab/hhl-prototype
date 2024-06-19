import numpy as np
import matplotlib.pyplot as plt
from hhl_prototype.solver.hhl import HHL
from qiskit.primitives import Estimator, Sampler
from qiskit.result import Counts


A = np.random.rand(4,4)
A = A+A.T

b = np.random.rand(4)

estimator = Estimator()
sampler = Sampler()


hhl = HHL(estimator)
#circuit = hhl.construct_circuit(A, b)

solution = hhl.solve(A,b)

print(np.linalg.solve(A,b))
print(solution.circuit_results)
