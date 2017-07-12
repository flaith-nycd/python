# https://mingrammer.com/introduce-comprehension-of-python
# a^2 + b^2 = c^2 (a < b < c)
solutions = [(x, y, z) for x in range(1, 30) for y in range(x, 30) for z in range(y, 30) if x**2 + y**2 == z**2]
print(solutions)

word = 'mathematics'
without_vowels = ''.join([c for c in word if c not in ['a', 'e', 'i', 'o', 'u']])
print(without_vowels)

matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
]
flatten = [e for r in matrix for e in r]
print(flatten)
