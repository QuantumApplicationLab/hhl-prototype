import numpy as np
import matplotlib.pyplot as plt
from hhl_prototype.solver.hhl import HHL
from qiskit.primitives import Estimator, Sampler
from qiskit.result import marginal_counts
from qiskit.quantum_info import Statevector

estimator = Estimator()
sampler = Sampler()

A = np.random.rand(4,4)
A = A+A.T
b = np.random.rand(4)

hhl = HHL(estimator, sampler = sampler)
solution = hhl.solve(A,b)

classical_solution = np.linalg.solve(A, b / np.linalg.norm(b))
ref_solution = classical_solution / np.linalg.norm(classical_solution)

circ = solution.circuit
circ.draw('mpl')

print(solution.state, ref_solution)
plt.show()

'''
matrix = np.array([[1, -1/3], [-1/3, 1]])
vector = np.array([1, 0])

sol2 = np.linalg.solve(matrix, vector / np.linalg.norm(vector))
refsol2 = sol2 / np.linalg.norm(sol2)

hhl_2 = HHL(estimator, sampler = sampler)
solution2 = hhl_2.solve(matrix, vector)

print(solution2.state, refsol2)
'''

"""
if sampler == None:
    print(np.real(Statevector(solution.state).data))
else: 
    for i in range(solution.qbits):
        print(np.real(np.sqrt(marginal_counts(solution.circuit_results.quasi_dists[0].binary_probabilities(), [i])['0'])))
"""

