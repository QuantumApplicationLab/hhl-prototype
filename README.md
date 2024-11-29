![Platform](https://img.shields.io/badge/platform-Linux-blue)
[![Python](https://img.shields.io/badge/Python-3.8-informational)](https://www.python.org/)
[![Qiskit](https://img.shields.io/badge/Qiskit-%E2%89%A5%200.44.2-6133BD)](https://github.com/Qiskit/qiskit)
[![License](https://img.shields.io/github/license/quantumapplicationlab/hhl-prototype?label=License)](https://github.com/quantumapplicationlab/hhl-prototype/blob/main/LICENSE.txt)
[![Code style: Black](https://img.shields.io/badge/Code%20style-Black-000.svg)](https://github.com/psf/black)
[![Tests](https://github.com/quantumapplicationlab/hhl-prototype/actions/workflows/coverage.yml/badge.svg)](https://github.com/quantumapplicationlab/hhl-prototype/actions/workflows/coverage.yml)
[![Coverage Status](https://coveralls.io/repos/github/QuantumApplicationLab/hhl-prototype/badge.svg?branch=main)](https://coveralls.io/github/QuantumApplicationLab/hhl-prototype?branch=main)

![hhl](./docs/hhl.png)

# HHL Quantum Linear Solver
The `hhl-prototype` allows to use the HHL algorithm to solve linear system of euqations. 
Original implementation was implemented by [@anedumla](https://github.com/anedumla) : https://github.com/anedumla/quantum_linear_solvers

## Installation
```python
git clone https://github.com/QuantumApplicationLab/hhl_prototype
cd hhl_prototype
pip install -e .
```

## Use

```python
import numpy as np
from hhl_prototype import HHL
from qiskit.primitives import Estimator, Sampler

# create the matrix
A = np.random.rand(4,4)
A = A+A.T

# create the right hand side 
b = np.random.rand(4)

# create the solver and solve
hhl = HHL(estimator=Estimator(), sampler=Sampler())
hhl.solve(A, b)
```



## Documentation
Tutorial: https://qiskit.org/textbook/ch-applications/hhl_tutorial.html
