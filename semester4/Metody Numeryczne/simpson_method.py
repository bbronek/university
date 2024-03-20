def f(x):
    return x**4+1

def simpson(x0, xn, n):
    h = (xn - x0) / (2*n)
    print(h)
    integration = f(x0) + f(xn)

    for i in range(1, 2*n):
        k = x0 + i * h
        print(k)
        if i % 2 == 0:
            integration = integration + 2 * f(k)
        else:
            integration = integration + 4 * f(k)

    # Finding final integration value
    integration = integration * h / 3

    return integration

lower_limit = float(input("Enter lower limit of integration: "))
upper_limit = float(input("Enter upper limit of integration: "))
sub_interval = int(input("Enter number of sub intervals: "))


result = simpson(lower_limit, upper_limit, sub_interval)
print("Integration result by Simpson's method is: %0.6f" % (result))
