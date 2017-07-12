#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from array import array
from random import sample

# Create an array of 255 bytes with random between 0 to 255
zpage = array('B', sample(range(0, 255), 255))

# Testing with values
zpage[30] = 0x20
zpage[31] = 0x58
zpage[32] = 0xFC

zpage[130] = 0x20
zpage[131] = 0x58
zpage[132] = 0xFC

zpage[230] = 0x20
zpage[231] = 0x58
zpage[232] = 0xFC

# Which values to find
values_to_find = [0x20, 0x58, 0xFC]

# # Create a set to be sure to have unique values
# set_of_values = set()
# Find all indexes
# indices_all = [[index for index, search in enumerate(zpage) if search == what] for what in values_to_find]
# print(sorted(indices_all))
# # Insert indexes found in our set
# for value in indices_all:
#     set_of_values |= set(value)
# # Sort our set
# set_of_values = sorted(set_of_values)
# print(set_of_values)

indices_all = [index for index, search in enumerate(zpage) for what in values_to_find if search == what]
set_of_values = sorted(indices_all)
# import itertools
#
# set_of_values = list(itertools.chain.from_iterable(indices_all))
# set_of_values = sorted(set_of_values)
print(set_of_values)

# Now we will need to keep the indexes that matched the values to find
# Inside our set, we need to extract the good indexes

# First we need to be sure to not iterate to the maximum
max_values_to_find = len(set_of_values) - len(values_to_find) + 1

# Init our list of results
result = []

# Loop to find
# If we found 12 values and our value to match is equal to 3
# max to find will be (12 - 3) + 1
for index in range(0, max_values_to_find):
    # Extract the exact length (value_to_find) from 0 to (12-3) + 1
    extract = set_of_values[index:index+len(values_to_find)]

    # Now the real checking
    index = extract[0]
    found = 0

    # We're checking each values found
    for values_index, zpage_index in enumerate(extract):
        # If we've found one, we add 1 to found
        if zpage[index] == values_to_find[values_index]:
            found += 1
        else:
            found -= 1
        index += 1

    # Then if we have found = to the length of the values_to_find
    # and add it to the list of results
    if found == len(values_to_find):
        result.append(extract)

print('Found {} times {} '.format(len(result), values_to_find))
print(result)

# Get indexes of each result
index = []
for x in range(0, len(result)):
    index.append(result[x][0])
print(index)
