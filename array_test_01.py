#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from array import array
from random import sample
from operator import itemgetter

# zpage = array('B', [0] * 255)

# Create an array of 255 bytes with random between 0 to 255
zpage = array('B', sample(range(0, 255), 255))

zpage[30] = 0x20
zpage[31] = 0x58
zpage[32] = 0xFC

zpage[130] = 0x20
zpage[131] = 0x58
zpage[132] = 0xFC

zpage[230] = 0x20
zpage[231] = 0x58
zpage[232] = 0xFC

# Show it
# for index, val in enumerate(zpage):
#     print('{:03d} - 0x{:02X}'.format(index, val))

# Value to search
value = 0x20
# How many in the array?
count_value = zpage.count(value)

# Get the index in zpage of the value we're searching
index = zpage.index(value)
print('First \'0x{:02X}\' is at position index \'{}\' in the array'.format(value, index))
print('And we can find it {} time(s)'.format(count_value))
indices = [index for index, search in enumerate(zpage) if search == value]
print(indices)

# Multiple find
values = [0x20, 0x58, 0xFC]
# indices_all = [index for index, search in enumerate(zpage) if values in search]
# print(indices_all)

# values = indices  # [0x20, 0x58, 0xFC]
# print(itemgetter(*values)(zpage))

# find = lambda searchList, elem: [[i for i, x in enumerate(searchList) if x == e] for e in elem]
# print(find(zpage, values))
indices_all = [[index for index, search in enumerate(zpage) if search == e] for e in values]
print(indices_all)
# print(indices_all[0])
# print(indices_all[1])
# print(indices_all[2])
s = set()
# s |= set(indices_all[0])
# s |= set(indices_all[1])
# s |= set(indices_all[2])
for value in indices_all:
    s |= set(value)
s = sorted(s)
print('   set=', s)

result = []
for x in s:
    result.append('{:02X}'.format(zpage[x]))

print('result=', result)
# ar = zip(indices_all[0], indices_all[1], indices_all[2])
# print(ar.__next__())
# print(ar.__next__())
# print(ar.__next__())

# l = []
# # l = [l.append(value) for value in indices_all]
# # print(l)
# for value in indices_all:
#     l.append(value)
# print(l)

# if values in zpage:
#     print('Found')
#
# print(values in zpage)

# my_list = ['abc-123', 'def-456', 'ghi-789', 'abc-456']
# things_to_find = ['abc', 'def']
# print([i for i, x in enumerate(my_list) if any(thing in x for thing in things_to_find)])


# def list_find(what, where):
#     """Find `what` list in the `where` list.
#
#     Return index in `where` where `what` starts
#     or -1 if no such index.
#
#     >>> f = list_find
#     >>> f([2, 1], [-1, 0, 1, 2])
#     -1
#     >>> f([-1, 1, 2], [-1, 0, 1, 2])
#     -1
#     >>> f([0, 1, 2], [-1, 0, 1, 2])
#     1
#     >>> f([1,2], [-1, 0, 1, 2])
#     2
#     >>> f([1,3], [-1, 0, 1, 2])
#     -1
#     >>> f([1, 2], [[1, 2], 3])
#     -1
#     >>> f([[1, 2]], [[1, 2], 3])
#     0
#     """
#     if not what:  # empty list is always found
#         return 0
#     try:
#         index = 0
#         while True:
#             index = where.index(what[0], index)
#             if where[index:index + len(what)] == what:
#                 return index  # found
#             index += 1  # try next position
#     except ValueError:
#         return -1  # not found
#
#
# def contains(what, where):
#     """Return [start, end+1] if found else empty list."""
#     i = list_find(what, where)
#     return [i, i + len(what)] if i >= 0 else []  # NOTE: bool([]) == False
#
# all_list = zpage.tolist()
# print(contains(values, all_list))

####################################
# WORK BT ONLY FIRST ###############
# def contains(small, big):
#     for i in range(len(big)-len(small)+1):
#         for j in range(len(small)):
#             if big[i+j] != small[j]:
#                 break
#         else:
#             return i, i+len(small)
#     return False
#
# start, end = contains(values, zpage)
# print(zpage[start:end])
#

print(len(s))
print(len(values))
print('----------')
checking_at = len(s) - len(values) + 1

last_check = []
for index in range(0, checking_at):
    extract = s[index:index+len(values)]

    print(extract)

    found = 0
    for values_index, zpage_index in enumerate(extract):
        if zpage[zpage_index] == values[values_index]:
            found += 1
        else:
            found -= 1
    if found == len(values):
        last_check.append(extract)

print(last_check)