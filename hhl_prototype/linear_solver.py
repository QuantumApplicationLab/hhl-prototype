# This code is part of Qiskit.
#
# (C) Copyright IBM 2021, 2022.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""An abstract class for linear systems solvers."""

from abc import ABC, abstractmethod
from typing import Union, Optional, List, Callable
import numpy as np

from qiskit import QuantumCircuit
#from qiskit.algorithms.algorithm_result import AlgorithmResult

#from .observables.linear_system_observable import LinearSystemObservable

# pylint: disable=too-few-public-methods