import math
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[1]


def main():
    methods = ROOT / "semester4/numerical-methods"
    load = lambda name: runpy.run_path(str(methods / name))
    bisection = load("bisection_method.py")["bisection"]
    assert math.isclose(bisection(0, 2, 1e-10), math.sqrt(2), abs_tol=1e-9)
    try:
        bisection(2, 3, 0.01)
    except ValueError:
        pass
    else:
        raise AssertionError("Unbracketed root accepted")
    assert load("horner.py")["horner"]([2, 3, 4], 2) == 18
    assert abs(load("secant_method.py")["secant"](1, 2) - math.sqrt(3)) < 0.01
    assert abs(load("tangent_method.py")["tangent_method"](2) - 1) < 0.1
    assert math.isclose(
        load("simpson_method.py")["simpson"](0, 1, 100), 1.2, abs_tol=1e-8
    )
    assert math.isclose(
        load("trapezoidal_method.py")["integral"](0, 1, 1000), 1 / 3, abs_tol=1e-6
    )
    try:
        import numpy as np
    except ImportError:
        print("SKIP SOR check: NumPy unavailable")
    else:
        solver = load("sor_solver.py")["sor_solver"]
        matrix = np.array([[4, 1, -1], [1, 3, 0], [-1, 0, 3]])
        target = np.array([3, -1, 1])
        guess = np.zeros(3, dtype=int)
        result = solver(matrix, target, 1.2, guess, 1e-10)
        assert np.allclose(matrix @ result, target)
        assert not guess.any()
    print("Semester 4 numerical checks passed")


if __name__ == "__main__":
    main()
