import numpy as np
import matplotlib.pyplot as plt
from hhl_prototype.solver.hhl import HHL
from qiskit.primitives import Estimator, Sampler
from qiskit.result import marginal_counts
from qiskit.quantum_info import Statevector

A = np.random.rand(4,4)
A = A+A.T

b = np.random.rand(4)
estimator = Estimator()
sampler = Sampler()


hhl = HHL(estimator, sampler = sampler)

solution = hhl.solve(A,b)
classical_solution = np.linalg.solve(A, b / np.linalg.norm(b))
ref_solution = classical_solution / np.linalg.norm(classical_solution)

print(ref_solution)
print(solution.vector)

"""
if sampler == None:
    print(np.real(Statevector(solution.state).data))
else: 
    for i in range(solution.qbits):
        print(np.real(np.sqrt(marginal_counts(solution.circuit_results.quasi_dists[0].binary_probabilities(), [i])['0'])))
"""

