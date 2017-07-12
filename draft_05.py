# -*- coding: utf-8 -*-


def extract_2bytes_from(data, from_index):
    low, high = data[from_index], data[from_index + 1]
    return (high << 8) + low


code = [0xA9, 0x20, 0xAD, 0xF8, 0x05]

result = extract_2bytes_from(code, 0)
print('Result: {:04x} - {}'.format(result, result))

values_to_find = [0x50, 0x52, 0x4F, 0x44, 0x4F, 0x53]
# result = ''.join("&markers=%s" % ','.join(map(str, x)) for x in values_to_find)
result = ['{:02x}'.format(x) for x in values_to_find]
print(result)

# Comprehension
code = [0xA9, 0x20, 0xAD, 0xF8, 0x05, 0x20, 0x58, 0xFC, 0xAD, 0xF8, 0x05, 0x20, 0xEA, 0x20, 0x58, 0xFC]
values_to_find = [0x20, 0x58, 0xFC]

indices_all = []
for index, search in enumerate(code):
    for what in values_to_find:
        if search == what:
            indices_all.append(index)

# indices_all = [index for index, search in enumerate(dsk.memdisk) for what in values_to_find if search == what]
print(indices_all)