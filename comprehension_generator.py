# https://mingrammer.com/introduce-comprehension-of-python
gen = (x ** 2 for x in range(10))
print(gen)
# <generator object <genexpr> at 0x105bde5c8>

print(next(gen))  # call 1
# 0

print(next(gen))  # call 2
# 1

print(next(gen))  # call 10
# 4

# ...

# if call 11th
# print(next(gen))  # call 11
#
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration
#

# Yes, it is an just generator. You can sum the yielding values.
gen = (x ** 2 for x in range(10))
sum_of_squares = sum(gen)
print(sum_of_squares)
