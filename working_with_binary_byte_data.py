"""
http://www.devdungeon.com/content/working-binary-data-python
"""
empty_bytes = bytes(4)
print(type(empty_bytes))
print(empty_bytes)

print(bin(22))

bytes_from_list = bytes([255, 254, 253, 252])
print(bytes_from_list)

i = int.from_bytes(bytes_from_list, byteorder='big')
print(i)

hex = "{0:x}".format(i)
print(hex)

print('---FORMAT STRING')
a_byte = b'\x7f'  # 127
i = ord(a_byte)  # Get the integer value of the byte

dec = "{0:d}".format(i)  # decimal: 127
bin = "{0:08b}".format(i)  # binary: 01111111
hex = "{0:x}".format(i)  # hexadecimal: 7f
oct = "{0:o}".format(i)  # octal: 177

print(dec)
print(bin)
print(hex)
print(oct)

print('---BITWISE OPERATION')
# Some bytes to play with
byte1 = int('11110000', 2)  # 240
byte2 = int('00001111', 2)  # 15
byte3 = int('01010101', 2)  # 85

# Ones Complement (Flip the bits)
print('~{}: {}'.format(byte1, ~byte1))

# AND
print('{} & {}: {}'.format(byte1, byte2, (byte1 & byte2)))
# OR
print('{} | {}: {}'.format(byte1, byte2, (byte1 | byte2)))

# XOR
print('{} ^ {}: {}'.format(byte1, byte3, (byte1 ^ byte3)))

# Shifting right will lose the right-most bit
print('{} >> 3: {}'.format(byte2, byte2 >> 3))

# Shifting left will add a 0 bit on the right side
print('{} << 1: {}'.format(byte2, byte2 << 1))

# See if a single bit is set
bit_mask = int('00000001', 2)  # Bit 1
print(bit_mask & byte1)  # Is bit set in byte1?
print(bit_mask & byte2)  # Is bit set in byte2?
