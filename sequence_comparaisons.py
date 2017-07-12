latest_python = (3, 7, 0)
# my_python = (3, 7, 0)
# my_python = (3, 6)
my_python = (3, 6, 1)

# zip used to combine iterables objects
# zip('ABCD', 'xy') --> Ax By
# https://docs.python.org/3/library/functions.html#zip
"""
for latest, my in zip(latest_python, my_python):
    if latest > my:
        msg = 'Update available'
        break
else:  # occures if there is no break
    msg = 'Up to date'
"""

# Simple if statement
"""
if latest_python > my_python:
    msg = 'Update available'
else:
    msg = 'Up to date'
"""

# Inline if-else statement, works with all kind of iterables objects (list, dict, tuples, set)
msg = 'Update available' if latest_python > my_python else 'Up to date'

# Result
print('Check update: %s' % msg)
