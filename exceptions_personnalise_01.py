class SplitError(Exception):
    pass


# Test 1 ---
# raise SplitError

# Test 2 ---

x = 1
y = 'a'

try:
    raise SplitError('Message d\'erreur test', x, y)
except SplitError as e:
    print(e.args)
