def y(x):
    return x ** 2

def integral(a, b, n):
    h = (b - a) / n
    sum = (y(a) + y(b))
    i = 1

    while i < n:
        sum += 2 * y(a + i * h)
        i += 1

    return ((h / 2) * sum)

print("Number of trapezoids:")
n = int(input())
print("x0:")
x0 = int(input())
print("xn:")
xn = int(input())

print("Result: "+ str(integral(x0, xn, n)))
