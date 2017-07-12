#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

# import json
#
# def file_json(value):
#     with open('op_value.json', 'w') as f:
#         for x in value.split():
#             # val = int(x, 16)
#             # json.dump(val, f)
#             json.dump(x, f)
#
# f = open('op_value.json', "r")
# code = json.load(f)
# f.close()
#
# print(code)

# print("""This program converts a sequence of ASCII numbers into,
# the string of text that it represents.\n""")
#
# inString = input("Please enter the ASCII-encoded message: ")
#
# message = "".join([chr(int(numStr)) for numStr in inString.split()])
#
# print("The decoded message is:", message)

IMPLICIT = 0
ACCUMULATOR = 1
IMMEDIATE = 2
ZERO_PAGE = 3
ZERO_PAGE_X = 4
ZERO_PAGE_Y = 5
RELATIVE = 6
ABSOLUTE = 7
ABSOLUTE_X = 8
ABSOLUTE_Y = 9
INDIRECT = 10
INDEXED_INDIRECT = 11
INDIRECT_INDEXED = 12


def get_addressing(addressing_mode):
    prefix = '#'
    postfix = ''

    if addressing_mode in (IMPLICIT, IMMEDIATE):
        prefix = '#$'
    elif addressing_mode in (ZERO_PAGE, ZERO_PAGE_X, ZERO_PAGE_Y, ABSOLUTE, ABSOLUTE_X, ABSOLUTE_Y):
        prefix = '$'
    elif addressing_mode in (INDIRECT, INDEXED_INDIRECT, INDIRECT_INDEXED):
        prefix = '($'

    if addressing_mode in (ZERO_PAGE_X, ABSOLUTE_X):
        postfix = ',X'
    elif addressing_mode in (ZERO_PAGE_Y, ABSOLUTE_Y):
        postfix = ',Y'
    elif addressing_mode == INDIRECT:
        postfix = ')'
    elif addressing_mode == INDEXED_INDIRECT:
        postfix = ',X)'
    elif addressing_mode == INDIRECT_INDEXED:
        postfix = '),Y'

    return prefix, postfix


def f_lda(adr_mode, value):
    # print('arg=%s - value=%s' % (arg, value))
    prefix, postfix = get_addressing(adr_mode)
    print('  LDA {}{}{}'.format(prefix, value, postfix))


def f_and(adr_mode, value):
    prefix, postfix = get_addressing(adr_mode)
    print('  AND {}{}{}'.format(prefix, value, postfix))


def f_sta(adr_mode, value):
    prefix, postfix = get_addressing(adr_mode)
    print('  STA {}{}{}'.format(prefix, value, postfix))


op6502 = dict()
#                     Addressing
#                           mode  Bytes
#                                    Cycles
#                                       Function
op6502['A5'] = ('LDA', ZERO_PAGE, 2, 3, f_lda)
op6502['A9'] = ('LDA', IMMEDIATE, 2, 2, f_lda)
op6502['29'] = ('AND', IMMEDIATE, 2, 2, f_and)
op6502['85'] = ('STA', ZERO_PAGE, 2, 3, f_sta)


# op6502['06'] = ('ASL', ZERO_PAGE, 2, 5, f_asl)
# op6502['26'] = ('ROL', ZERO_PAGE, 2, 5, f_rol)
# op6502['69'] = ('ADC', IMMEDIATE, 2, 2, f_adc)
# op6502['60'] = ('RTS', IMPLICIT, 1, 6, f_rts)

# opcode = 'A9'
# args = op6502[opcode]
# assert len(args) == 5
# print(len(args))
# for index, val in enumerate(args):
#     print(index, val)
# # args[1](args[0])
# args[4](args[1], 'A0')

def gen_line(opcode, value):
    args = op6502[opcode]
    args[4](args[1], value)


gen_line('A9', 'A0')
gen_line('A5', 'A0')
gen_line('29', 'A0')
gen_line('85', 'A0')


# AD F8 05    LDA   $05F8
# 8D BA 0B    STA   $0BBA
# 8D AC 0B    STA   $0BAC
# 4A          LSR
# 4A          LSR
# 4A          LSR
# 4A          LSR
# 09 C0       ORA   #$C0
# 8D F3 03    STA   $03F3
# 49 A5       EOR   #$A5
# 8D F4 03    STA   $03F4
# A9 00       LDA   #$00
# 8D F2 03    STA   $03F2
# A9 FF       LDA   #$FF
# 85 D6       STA   $D6
# AD 00 08    LDA   $0800
# C9 A2       CMP   #$A2
# D0 03       BNE   $302A
# 4C 00 08    JMP   $0800
# 6C F2 00    JMP   ($00F2)

def extract_from_pc(bytes_to_extract):
    global pc
    global code
    byte = ''

    # try:
    extract_at_pos = pc + bytes_to_extract  # 6
    opcode = code[pc]
    print(code[pc:extract_at_pos])
    print('pc:', pc, ' extract_at_pos:', extract_at_pos)

    pc += 1  # 4
    # TRY WITH
    if pc >= len(code):
        print('max-----------------------------------')
        pc = len(code) - 1
        extract_at_pos = pc

    if bytes_to_extract == 3:
        #      code[4, 6]
        low, high = code[pc:extract_at_pos]
        # swap
        byte = high + low
        # pc += 1
    else:
        # a = code[extract_at_pos - 1]
        byte = code[pc]
        # try:
        #     byte = code[pc]
        # except Exception as error:
        #     print('Caught this error: ' + repr(error) + ' - pc:' + str(pc) + ' max=' + str(len(code)-1))
        #     sys.exit()
    # *********************************************
    # ***  ISSUE HERE, WHEN ARRIVED AT THE END
    # ***  extract_at_pos = 29, max is 28
    pc = extract_at_pos

    # # TRY WITH
    # if pc >= len(code):
    #     print('max-----------------------------------')
    #     pc = len(code) - 1

    print('opcode:',opcode,'= byte:', byte)
    print('pc:', pc, ' code:', code[pc])
    print('******************')
    # except:
    #     # pass
    #     print('Error pc=',pc)
    #     sys.exit()


# op = 'A9 20 AD F8 05 8D BA 0B 8D AC 0B 4A 4A 4A 4A 09 C0 8D F3 03 49 A5 8D F4 03 A9 00 8D F2 03 A9 FF 85 D6' \
#      ' AD 00 08 C9 A2 D0 03 4C 00 08 6C F2 00'
#
# code_to_disasm = ['A9', '20', 'AD', 'F8', '05', '8D', 'BA', '0B', '8D', 'AC', '0B', '4A', '4A', '4A', '4A', '09',
#                   'C0', '8D', 'F3', '03', '49', 'A5', '8D', 'F4', '03', 'A9', '00', '8D', 'F2', '03', 'A9', 'FF',
#                   '85', 'D6', 'AD', '00', '08', 'C9', 'A2', 'D0', '03', '4C', '00', '08', '6C', 'F2', '00']
#
#
# code = op.upper().strip().split()
#
# if code == code_to_disasm:
# test with opcode 8D BA 0B :
#  STA $0BBA
#                       Addressing
#                           mode   Bytes
#                                     Cycles
# op6502['8D'] = ('STA', ABSOLUTE, 3, 4)

# print('******************')
#
# pc = 0
# bytes_to_extract = 2
# extract_at_pos = pc + bytes_to_extract  # 6
# print(code[pc:extract_at_pos])
# print('pc:', pc)
#
# pc += 1  # 4
#
# if bytes_to_extract == 3:
#     #      code[4, 6]
#     low, high = code[pc:extract_at_pos]
#     # swap
#     byte = high + low
#     # pc += 1
# else:
#     # a = code[extract_at_pos - 1]
#     byte = code[pc]
# pc = extract_at_pos
#
# print('byte:', byte)
# print('pc:', pc, ' code:', code[pc])
#
# print('******************')
#
# bytes_to_extract = 3
# extract_at_pos = pc + bytes_to_extract  # 6
# print('pc:', pc)
# print(code[pc:extract_at_pos])
#
# pc += 1  # 4
#
# if bytes_to_extract == 3:
#     #      code[4, 6]
#     low, high = code[pc:extract_at_pos]
#     # swap
#     byte = high + low
#     # pc += 1
# else:
#     # a = code[extract_at_pos - 1]
#     byte = code[pc]
# pc = extract_at_pos
#
# print('byte:', byte)
# print('pc:', pc, ' code:', code[pc])

# extract_from_pc(2)
# extract_from_pc(3)
# extract_from_pc(3)
# extract_from_pc(3)
# extract_from_pc(1)

# pc:
#  0: A9 A0     LDA   #$A0
#  2: 29 7F     AND   #$7F          ; ACC = $A0 : And $7F => $20
#  4: 85 1E     STA   $1E           ; = $20 %00100000
#  6: A9 00     LDA   #$00
#  8: 85 1F     STA   $1F           ; $1F = 00
# 10: 06 1E     ASL   $1E           ; %01000000
# 12: 26 1F     ROL   $1F           ; 00
# 14: 06 1E     ASL   $1E           ; %10000000
# 16: 26 1F     ROL   $1F           ; 00
# 18: 06 1E     ASL   $1E           ; %00000000 : La retenue est mise
# 20: 26 1F     ROL   $1F           ; 00
# 22: A5 1F     LDA   $1F
# 24: 69 B3     ADC   #$B3
# 26: 85 1F     STA   $1F           ; $1F = $B4 (il y a la retenue)
# 28: 60        RTS                 ; $1E = $00

# op = 'a9 a0 29 7f 85 1e A9 00 85 1f 06 1e 26 1f 06 1e 26 1f 06 1e 26 1f A5 1f 69 b3 85 1f 60'
# u = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]

op = 'A9 20 AD F8 05 8D BA 0B 8D AC 0B 4A 4A 4A 4A 09 C0 8D F3 03 49 A5 8D F4 03 A9 00 8D F2 03 A9 FF 85 D6' \
     ' AD 00 08 C9 A2 D0 03 4C 00 08 6C F2 00'
u = [2, 3, 3, 3, 1, 1, 1, 1, 2, 3, 2, 3, 2, 3, 2, 2, 3, 2, 2, 3, 3]

code = op.upper().strip().split()
print('Code length = ' + str(len(code) - 1))
print('******************')
pc = 0

for i in u:
    extract_from_pc(i)
