def tangent_method(x, tolerance=0.01, max_iterations=100):
    if tolerance <= 0:
        raise ValueError("Tolerance must be positive")
    for _ in range(max_iterations):
        value = x**3 - 3 * x + 2
        if abs(value) < tolerance:
            return x
        derivative = 3 * x**2 - 3
        if derivative == 0:
            raise ValueError("Derivative is zero")
        x -= value / derivative
    raise RuntimeError("Newton's method did not converge")


if __name__ == "__main__":
    print(f"Root: {tangent_method(2):.4f}")
