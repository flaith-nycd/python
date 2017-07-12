# https://mingrammer.com/introduce-comprehension-of-python
from math import sqrt
non_squars = [x for x in range(101) if sqrt(x)**2 != x]

epithets = ['sweet', 'annoying', 'cool', 'grey-eyed']
names = ['john', 'alice', 'james']
epithet_names = [(e, n) for e in epithets for n in names]
print(epithet_names)
