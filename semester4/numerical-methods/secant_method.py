import math

EPS0 = 0.01 # accuracy of the comparison with zero
EPSX = 0.01 # accuracy of determining the root

def f(x):
   return x**3+x**2-3*x-3

x1 = 1
x2 = 2
print ("Result:")


f1 = f(x1)
f2 = f(x2)
i = 15 

while (i > 0) and (abs(x1 - x2) > EPSX):
    if abs(f1 - f2) < EPS0:
        print("Error: Wrong intial points")
        i = 0
        break
    x0 = x1 - f1 * (x1 - x2) / (f1 - f2)
    f0 = f(x0)
    if abs(f0) < EPS0: break
    x2, f2 = x1, f1
    x1, f1 = x0, f0
    i -= 1
    if i == 0: print ("Error: Limit exceeded")

if i > 0: print("x0 = %15.8f" % x0)
