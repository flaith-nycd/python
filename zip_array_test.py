def int2ascii(char):
    if char in range(32, 128):  # Check from ascii code $20 to $7E
        return chr(char)
    elif char in range(160, 255):  # if between $A0 to $FE
        return chr(char - 128)  # Substract $80 to go back between $20 to $7E
    else:
        return '.'


def split_array(array, size):
    return [array[i:i + size] for i in range(0, len(array), size)]


def generate(arraylist, size=16):
    header = []
    header.append('   ')
    for i in range(size):
        header.append('{:02X} '.format(i))
    header.append('-' * size)
    # header.append('\n')
    header = ''.join(header)

    hexa_list = []
    for char in arraylist:
        hexa_list.append("{:02X}".format(char))
    hexa_list = ' '.join(hexa_list)

    char_list = []
    for char in arraylist:
        char_list.append(int2ascii(char))
    char_list = ''.join(char_list)

    result_list = split_array(hexa_list, size * 2 + size)
    result_char = split_array(char_list, size)

    return header, result_list, result_char


array_list = [193, 196, 210, 141, 160, 202, 205, 208, 160, 199, 207, 208, 210, 201, 206, 212, 141, 141, 205, 193, 203,
              197, 193, 196, 210, 160, 204, 196, 193, 160, 208, 207, 211, 217, 141, 160, 212, 193, 216, 141, 160, 204,
              196, 193, 160, 194, 193, 211, 172, 216, 141, 160, 211, 212, 193, 160, 193, 196, 210, 141, 160, 204, 196,
              193, 160, 200, 193, 213, 212, 172, 216, 141, 160, 211, 212, 193, 160, 193, 196, 210, 171, 177, 141, 160,
              210, 212, 211, 141, 141, 199, 207, 208, 210, 201, 206, 212, 160, 204, 196, 193, 160, 208, 207, 211, 216,
              141, 170, 170, 170, 32, 196, 197, 194, 213, 212, 32, 193, 202, 207, 213, 212, 141, 160, 193, 211, 204,
              141, 160, 193, 211, 204, 141, 170, 170, 170, 32, 198, 201, 206, 32, 193, 202, 207, 213, 212, 141, 160,
              212, 193, 216, 141, 160, 204, 196, 217, 160, 163, 164, 176, 176, 141, 195, 207, 206, 212, 208, 210, 201,
              206, 160, 204, 196, 193, 160, 164, 176, 176, 176, 176, 172, 217, 160, 187, 193, 196, 210, 197, 211, 211,
              197, 32, 196, 213, 32, 195, 193, 210, 193, 195, 212, 197, 210, 197, 141, 141, 160, 211, 212, 193, 160,
              168, 193, 196, 210, 172, 216, 169, 160, 187, 193, 196, 210, 197, 211, 211, 197, 32, 196, 197, 32, 204,
              193, 32, 204, 201, 199, 206, 197, 32, 199, 210, 193, 208, 200, 201, 209, 213, 197, 141, 141, 160, 201,
              206, 217, 160, 160]

# hexa = ''
# char_list = []
# for char in enumerate(array_list):
#     char_list.append(int2ascii(char))
#
# char_list = ''.join(char_list)
# print(char_list)
#
# zipped_value = zip(*[iter(array_list)] * 16)
# zipped_char = zip(*[iter(char_list)] * 16)
#
# result_list = list(zipped_value)
# result_char = list(zipped_char)
# print(result_list)
# print(result_char)

# for index,value in enumerate(result_list):
#     print(value, ' - ', result_char[index])
size = 16
list_header, list_byte, list_text = generate(array_list, size)

print(list_header)
# index = 0
# for item1, item2 in zip(list_byte, list_text):
#     print('{:02X}:{} {}'.format(index, item1.strip(), item2))
#     index += 1
for index, (item1, item2) in enumerate(zip(list_byte, list_text)):
    print('{:02X}:{} {}'.format(index, item1.strip(), item2))

# OR
# print(), print('itertools')
# from itertools import count
#
# for i, a, b in zip(count(), list_byte, list_text):
#     print('{:02X}:{} {}'.format(i, a.strip(), b))
