import sympy as sym
import numpy as np


def tangent_method(x):
    func = np.poly1d([1,0,-3,2])
    derivFunc = func.deriv()

    h =  func(x)/derivFunc(x)
    eps = 0.01
    i = 0
    temp_x = 0
    while abs(func(x)) >= eps or abs(x-temp_x) >= eps:
        h = func(x)/derivFunc(x)
        temp_x=x
        x = x - h
        i = i+1
     
    print("The value of the root is : ", "%.4f"% x)
    print("Iterations= "+ str(i))

x0 = 2 # Initial value
tangent_method(x0)
