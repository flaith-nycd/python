import random

print('-' * 30, ' 7 lines')

grid = range(1, 51)  # Grile allant de 1 a 50 inclus
star = range(1, 13)  # Etoile allant de 1 a 12 inclus

result_grid = sorted(random.sample(grid, 5))
result_star = sorted(random.sample(star, 2))

print('Grid: {}'.format(result_grid))
print('Star: {}'.format(result_star))

print('-' * 30, ' 5 lines')

result_grid = sorted(random.sample(range(1, 51), 5))
result_star = sorted(random.sample(range(1, 13), 2))

print('Grid: {}'.format(result_grid))
print('Star: {}'.format(result_star))

print('-' * 30, ' 3 lines')

print('Grid: {}'.format(sorted(random.sample(range(1, 51), 5))))
print('Star: {}'.format(sorted(random.sample(range(1, 13), 2))))
