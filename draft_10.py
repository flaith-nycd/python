# Pointers


def memory_address(var):
    return hex(id(var))

# 2 vars with same values
a = 4
b = 4

# But results: Same address
print(memory_address(a))
print(memory_address(b))
