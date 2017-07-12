#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Byteorder is 'little-endian' for 6502

Get each byte and convert to integer
ex:
    a  b  c
    7D 42 06 should be: 06427D = 410237
so
    c      b     a
    06     42    7D
    
    << 16  << 8  << 0

if 4 bytes, we have 

    (d << 24) + (c << 16) + (b << 8) + (a)
"""


# First way to convert
def reverse_byte(data):
    return int(''.join(['{:02X}'.format(i) for i in data[::-1]]), 16)


byte = [0x7d, 0x42, 0x06]
rb = reverse_byte(byte)
print('1-Reversed: ${:010X}-{}'.format(rb, rb))

byte = [0x7d, 0x42, 0x06, 0x01]
rb = reverse_byte(byte)
print('1-Reversed: ${:010X}-{}'.format(rb, rb))

# Second way to convert
shift_value = [0, 8, 16, 24, 32, 40, 48, 56, 64]


def convert_from_byte(data):
    result = 0
    for index, one_byte in enumerate(data):
        result += one_byte << shift_value[index]
    return result


byte = [0x7d, 0x42, 0x06, 0x01]
WIDTH = len(byte)
value = convert_from_byte(byte)
print('2-Value of {} = ${:0{width}X}({})'.format(byte, value, value, width=WIDTH * 2))


# Third way to convert


def convert_from_byte(data):
    result = 0
    for index, one_byte in enumerate(data):
        result += one_byte << index * 8
    return result


byte = [0x7d, 0x42, 0x06, 0x01]
WIDTH = len(byte)
value = convert_from_byte(byte)
print('3-Value of {} = ${:0{width}X}({})'.format(byte, value, value, width=WIDTH * 2))

byte = [0x7d]
WIDTH = len(byte)
value = convert_from_byte(byte)
print('3-Value of {} = ${:0{width}X}({})'.format(byte, value, value, width=WIDTH * 2))


# Fourth way to convert with params: from, how many byte to extract and convert


def convert_from_byte(data, from_index=0x00, how_many_byte=None):
    result = 0
    if how_many_byte is None:
        to_index = None
    else:
        to_index = from_index + how_many_byte

    # byte_to_extract = data[from_index:to_index]
    #
    # print('4-Extracted: {} from {}'.format(byte_to_extract, data))
    # for index, one_byte in enumerate(byte_to_extract):
    for index, one_byte in enumerate(data[from_index:to_index]):
        result += one_byte << index * 8
    return result


byte = [0x7d, 0x42, 0x06, 0x01]
WIDTH = len(byte)
value = convert_from_byte(byte, 1, 2)
print('4-Value of {} = ${:0{width}X}({})'.format(byte[1:3], value, value, width=WIDTH * 2))

byte = [0x7d]
WIDTH = len(byte)
value = convert_from_byte(byte)
print('4-Value of {} = ${:0{width}X}({})'.format(byte, value, value, width=WIDTH * 2))

# Test valid chars with function 'all', check other function 'any'
valid_char = ' abcdefghijklmnopqrstuvwxyz'
# valid_char = '0123456789ABCDEF'
test = 'couirttj r'
# if not all([var in valid_char for var in test.upper()]):
if not all([var in valid_char for var in test]):
    print('Invalid string')
else:
    print('Valid string')
