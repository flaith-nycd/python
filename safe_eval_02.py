#!/usr/bin/env python
from math import *

hidden_value = "this is secret"


def dangerous_function(filename):
    print(open(filename).read())


user_func = input("type a function: y = ")

for x in range(1, 10):
    print("x = ", x, ", y = ", eval(user_func))

"""
type a function: y = dir()
x =  1 , y =  ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', 
'__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 
'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 
'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 
'modf', 'nan', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'user_func', 'x']
"""