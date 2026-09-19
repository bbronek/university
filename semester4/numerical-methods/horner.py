def horner(coefficients, x):
    result = 0
    for coefficient in coefficients:
        result = result * x + coefficient
    return result


if __name__ == "__main__":
    degree = int(input("Polynomial degree: "))
    coefficients = list(
        map(float, input("Coefficients, highest degree first: ").split())
    )
    if degree < 0 or len(coefficients) != degree + 1:
        raise ValueError("Expected degree + 1 coefficients")
    x = float(input("x: "))
    print("f(x) =", horner(coefficients, x))
