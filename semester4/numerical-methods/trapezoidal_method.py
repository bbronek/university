def y(x):
    return x**2


def integral(lower, upper, intervals):
    if intervals <= 0:
        raise ValueError("The number of intervals must be positive")
    step = (upper - lower) / intervals
    total = (y(lower) + y(upper)) / 2
    total += sum(y(lower + index * step) for index in range(1, intervals))
    return step * total


if __name__ == "__main__":
    intervals = int(input("Number of trapezoids: "))
    lower = float(input("Lower integration limit: "))
    upper = float(input("Upper integration limit: "))
    print("Integral:", integral(lower, upper, intervals))
