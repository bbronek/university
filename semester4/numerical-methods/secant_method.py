def f(x):
    return x**3 + x**2 - 3 * x - 3


def secant(first, second, tolerance=0.01, max_iterations=100):
    if tolerance <= 0:
        raise ValueError("Tolerance must be positive")
    for _ in range(max_iterations):
        first_value, second_value = f(first), f(second)
        if abs(second_value) < tolerance:
            return second
        if first_value == second_value:
            raise ValueError("Secant points have equal function values")
        next_point = second - second_value * (second - first) / (
            second_value - first_value
        )
        first, second = second, next_point
    raise RuntimeError("Secant method did not converge")


if __name__ == "__main__":
    print(f"Root: {secant(1, 2):.8f}")
