# https://mingrammer.com/introduce-comprehension-of-python
evens = [x * 2 for x in range(11)]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

vals = [32, 12, 96, 42, 32, 93, 31, 23, 65, 43, 76]
amount = sum(vals)
norm_and_move = [(x / amount) + 1 for x in vals]
print(norm_and_move)
