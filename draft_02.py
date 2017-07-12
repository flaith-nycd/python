#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

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


def extract_from_pc(bytes_to_extract):
    global pc
    global code
    byte = ''

    # try:
    extract_at_pos = pc + bytes_to_extract  # 6
    opcode = code[pc]
    print('      ', code[pc:extract_at_pos])
    print('pc: [' + str(pc) + '] - extract_at_pos: ' + str(extract_at_pos))

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

    print('------ opcode: ' + opcode + ' --- byte: $' + byte)
    print('pc: [' + str(pc) + '] - code: $' + code[pc])

    # except:
    #     # pass
    #     print('Error pc=',pc)
    #     sys.exit()


# A9 A0     LDA   #$A0
# 29 7F     AND   #$7F          ; ACC = $A0 : And $7F => $20
# 85 1E     STA   $1E           ; = $20 %00100000
# A9 00     LDA   #$00
# 85 1F     STA   $1F           ; $1F = 00
# 06 1E     ASL   $1E           ; %01000000
# 26 1F     ROL   $1F           ; 00
# 06 1E     ASL   $1E           ; %10000000
# 26 1F     ROL   $1F           ; 00
# 06 1E     ASL   $1E           ; %00000000 : La retenue est mise
# 26 1F     ROL   $1F           ; 00
# A5 1F     LDA   $1F
# 69 B3     ADC   #$B3
# 85 1F     STA   $1F           ; $1F = $B4 (il y a la retenue)
# 60        RTS                 ; $1E = $00
# op = 'a9 a0 29 7f 85 1e A9 00 85 1f 06 1e 26 1f 06 1e 26 1f 06 1e 26 1f A5 1f 69 b3 85 1f 60'
# u = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]

# A9 20       LDA   #$20
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
op = 'A9 20 AD F8 05 8D BA 0B 8D AC 0B 4A 4A 4A 4A 09 C0 8D F3 03 49 A5 8D F4 03 A9 00 8D F2 03 A9 FF 85 D6' \
     ' AD 00 08 C9 A2 D0 03 4C 00 08 6C F2 00'
u = [2, 3, 3, 3, 1, 1, 1, 1, 2, 3, 2, 3, 2, 3, 2, 2, 3, 2, 2, 3, 3]

code = op.upper().strip().split()
print('Code length = ' + str(len(code) - 1))
print('******************')
pc = 0

for i in u:
    extract_from_pc(i)
