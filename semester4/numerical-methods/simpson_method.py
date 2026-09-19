def f(x):
    return x**4 + 1


def simpson(lower, upper, pairs):
    if pairs <= 0:
        raise ValueError("The number of interval pairs must be positive")
    step = (upper - lower) / (2 * pairs)
    total = f(lower) + f(upper)
    for index in range(1, 2 * pairs):
        total += (4 if index % 2 else 2) * f(lower + index * step)
    return total * step / 3


if __name__ == "__main__":
    lower = float(input("Lower integration limit: "))
    upper = float(input("Upper integration limit: "))
    pairs = int(input("Number of interval pairs: "))
    print(f"Simpson integral: {simpson(lower, upper, pairs):.6f}")
