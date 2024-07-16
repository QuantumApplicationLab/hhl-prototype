from abc import ABC, abstractmethod
from typing import Union, Optional, List, Callable
import numpy as np

from qiskit import QuantumCircuit
from qiskit.result import Result
from qiskit.quantum_info.operators.base_operator import BaseOperator


class HHLResult:
    """A base class for linear systems results.

    The linear systems algorithms return an object of the type ``LinearSystemsResult``
    with the information about the solution obtained.
    """

    def __init__(self) -> None:
        super().__init__()

        # Set the default to None, if the algorithm knows how to calculate it can override it.
        self._state = None
        self._observable = None
        self._euclidean_norm = None
        self._circuit_results = None
        self._qbits = None
        self._solution = None

    @property
    def observable(self) -> Union[float, List[float]]:
        """return the (list of) calculated observable(s)"""
        return self._observable

    @observable.setter
    def observable(self, observable: Union[float, List[float]]) -> None:
        """Set the value(s) of the observable(s).

        Args:
            observable: The new value(s) of the observable(s).
        """
        self._observable = observable

    @property
    def circuit(self) -> Union[QuantumCircuit, np.ndarray]:
        """return either the circuit that prepares the solution or the solution as a vector"""
        return self._circuit

    @circuit.setter
    def circuit(self, circuit: Union[QuantumCircuit, np.ndarray]) -> None:
        """Set the solution state as either the circuit that prepares it or as a vector.

        Args:
            state: The new solution state.
        """
        self._circuit = circuit

    @property
    def solution(self) -> np.ndarray:
        """return either the circuit that prepares the solution or the solution as a vector"""
        return self._state

    @solution.setter
    def solution(self, solution: np.ndarray) -> None:
        """Set the solution state as either the circuit that prepares it or as a vector.

        Args:
            state: The new solution state.
        """
        self._solution = solution

    @property
    def state(self) -> Union[QuantumCircuit, np.ndarray]:
        """return either the circuit that prepares the solution or the solution as a vector"""
        return self._state

    @state.setter
    def state(self, state: Union[QuantumCircuit, np.ndarray]) -> None:
        """Set the solution state as either the circuit that prepares it or as a vector.

        Args:
            state: The new solution state.
        """
        self._state = state

    @property
    def euclidean_norm(self) -> float:
        """return the euclidean norm if the algorithm knows how to calculate it"""
        return self._euclidean_norm

    @euclidean_norm.setter
    def euclidean_norm(self, norm: float) -> None:
        """Set the euclidean norm of the solution.

        Args:
            norm: The new euclidean norm of the solution.
        """
        self._euclidean_norm = norm

    @property
    def qbits(self) -> int:
        """return the euclidean norm if the algorithm knows how to calculate it"""
        return self._qbits

    @qbits.setter
    def qbits(self, count: int) -> None:
        """Set the euclidean norm of the solution.

        Args:
            norm: The new euclidean norm of the solution.
        """
        self._qbits = count

    @property
    def x_reg(self) -> int:
        """return the euclidean norm if the algorithm knows how to calculate it"""
        return self._x_reg

    @qbits.setter
    def x_reg(self, count: int) -> None:
        """Set the euclidean norm of the solution.

        Args:
            norm: The new euclidean norm of the solution.
        """
        self._x_reg = count

    @property
    def circuit_results(self) -> Union[List[float], List[Result]]:
        """return the results from the circuits"""
        return self._circuit_results

    @circuit_results.setter
    def circuit_results(self, results: Union[List[float], List[Result]]):
        self._circuit_results = results

    @property
    def vector(self) -> np.array:
        """return the euclidean norm if the algorithm knows how to calculate it"""
        return self._qbits

    @vector.setter
    def vector(self, solution: np.array) -> None:
        """Set the euclidean norm of the solution.

        Args:
            norm: The new euclidean norm of the solution.
        """
        self._vector = solution
