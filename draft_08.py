# -*- coding: utf-8 -*-

for i in range(10):
    print(i, end=', ')
print()
print()

print(*range(10), sep=', ')
print()

print(", ".join([str(i) for i in range(10)]))
print()

val = ['a', 'b', 'c', 'd', 'e']
print(*val, sep=' · ')  # alt 250
