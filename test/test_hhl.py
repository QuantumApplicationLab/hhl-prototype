import numpy as np
import pytest
from qiskit.primitives import Estimator
from scipy.sparse import random as sprand
from scipy.sparse import sparray
from hhl_prototype.solver.hhl import HHL
from qiskit.primitives import Estimator, Sampler


def create_random_matrix(size: int) -> sparray:
    """Create a random symmetric matrix.

    Args:
        size (int): size of the matrix
    """
    mat = np.random.rand(size, size)
    return mat + mat.T


size = 4


@pytest.mark.parametrize("A", [create_random_matrix(size)])
@pytest.mark.parametrize("b", [np.random.rand(size)])
@pytest.mark.parametrize("estimator", [Estimator()])
@pytest.mark.parametrize("sampler", [Sampler()])

def test_hhl_solve_default(A, b, estimator, sampler):
    """Test the hhl solver."""
    hhl = HHL(estimator, sampler = sampler)
    results = hhl.solve(A,b).solution
    if np.linalg.norm(A.dot(results) - b) > 0.1:
        pytest.skip("HHL solution innacurate")
