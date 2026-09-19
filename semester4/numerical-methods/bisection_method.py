def f(x):
    return x**2 - 2


def bisection(left, right, tolerance, max_iterations=1000):
    if tolerance <= 0 or left > right or f(left) * f(right) > 0:
        raise ValueError("Expected a bracketed root and a positive tolerance")
    if f(left) == 0:
        return left
    if f(right) == 0:
        return right
    for _ in range(max_iterations):
        middle = (left + right) / 2
        if f(middle) == 0 or (abs(f(middle)) < tolerance and right - left < tolerance):
            return middle
        if f(left) * f(middle) < 0:
            right = middle
        else:
            left = middle
    raise RuntimeError("Bisection did not converge")


if __name__ == "__main__":
    left = float(input("Left endpoint: "))
    right = float(input("Right endpoint: "))
    tolerance = float(input("Tolerance: "))
    print(f"Root: {bisection(left, right, tolerance):.8f}")
