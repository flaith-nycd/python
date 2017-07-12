array_char = {}
for index_char in range(10):
    # array_char = {index_char: []}
    array_char[index_char] = [[index_char, 1, 1, 1, 0, 0], [1, 0, 0, 0, 1, 0]]

print(array_char[2])
print(array_char)
print(type(array_char))