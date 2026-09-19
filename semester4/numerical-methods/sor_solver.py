import numpy as np


def sor_solver(matrix, target, omega, initial_guess, tolerance, max_iterations=10000):
    matrix = np.asarray(matrix, dtype=float)
    target = np.asarray(target, dtype=float)
    solution = np.array(initial_guess, dtype=float, copy=True)
    if (
        matrix.ndim != 2
        or matrix.shape != (len(target), len(target))
        or solution.shape != target.shape
    ):
        raise ValueError("Matrix and vector dimensions do not match")
    if not 0 < omega < 2 or tolerance <= 0 or np.any(np.diag(matrix) == 0):
        raise ValueError("Invalid relaxation, tolerance, or matrix diagonal")
    for _ in range(max_iterations):
        residual = np.linalg.norm(matrix @ solution - target)
        if not np.isfinite(residual):
            raise RuntimeError("SOR diverged")
        if residual <= tolerance:
            return solution
        for row in range(len(target)):
            remainder = matrix[row] @ solution - matrix[row, row] * solution[row]
            solution[row] = (1 - omega) * solution[row] + omega * (
                target[row] - remainder
            ) / matrix[row, row]
    raise RuntimeError("SOR did not converge")


if __name__ == "__main__":
    matrix = np.array([[4, 1, -1], [1, 3, 0], [-1, 0, 3]])
    target = np.array([3, -1, 1])
    print(sor_solver(matrix, target, 1.2, np.zeros(3), 1e-10))
