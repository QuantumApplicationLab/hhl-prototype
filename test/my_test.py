import numpy as np
import matplotlib.pyplot as plt
from hhl_prototype.solver.hhl import HHL
from qiskit.primitives import Estimator, Sampler
from qiskit.result import marginal_counts
from qiskit.quantum_info import Statevector
from qiskit.quantum_info import SparsePauliOp

# A = np.random.rand(4, 4)
# A = A + A.T
# b = np.random.rand(4)

A = np.array(
    [
        [1, -1 / 3, 0, 0],
        [-1 / 3, 1, -1 / 3, 0],
        [0, -1 / 3, 1, -1 / 3],
        [0, 0, -1 / 3, 1],
    ]
)
b = np.array([1, 0, 0, 0])

A = np.array([[1, -1 / 3], [-1 / 3, 1]])
b = np.array([1, 1 / 2])


estimator = Estimator()
sampler = Sampler()


hhl = HHL(estimator, sampler=sampler)

solution = hhl.solve(A, b)
cs = np.linalg.solve(A, b)

print(cs)
print(solution.solution)
