#!/usr/bin/env python
from math import *

user_func = input("type a function: y = ")

for x in range(1, 10):
    print("x = ", x, ", y = ", eval(user_func))

"""
type a function: y = sin(x)
x =  1 , y =  0.8414709848078965
x =  2 , y =  0.9092974268256817
x =  3 , y =  0.1411200080598672
x =  4 , y =  -0.7568024953079282
x =  5 , y =  -0.9589242746631385
x =  6 , y =  -0.27941549819892586
x =  7 , y =  0.6569865987187891
x =  8 , y =  0.9893582466233818
x =  9 , y =  0.4121184852417566
"""