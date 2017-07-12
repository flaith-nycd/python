import time

# code = ['A9', 'A0', 'AD', 'F8', '05', '4A', '4A', '86', 'D6', 'EA', '60']
# code = ['A9', '20', 'AD', 'F8', '05', '8D', 'BA', '0B', '8D', 'AC', '0B', '4A', '4A', '4A', '4A', '09', 'C0', '8D',
#         'F3', '03', '49', 'A5', '8D', 'F4', '03', 'A9', '00', '8D', 'F2', '03', 'A9', 'FF', '85', 'D6', 'AD', '00',
#         '08', 'C9', 'A2', 'D0', '03', '4C', '00', '08', '6C', 'F2', '00']
code = ['A9', '20', 'AD', 'F8', '05', '8D', 'BA', '0B', '8D', 'AC', '0B', '4A', '4A', '4A', '4A', '09', 'C0', '8D',
        'F3', '03', '49', 'A5', '8D', 'F4', '03', 'A9', '00', '8D', 'F2', '03', 'A9', 'FF', '85', 'D6', 'AD', '00',
        '08', 'C9', 'A2', 'D0', '03', '4C', '00', '08', 'EA', '00', '6C', 'F2', '00', '60']

extract_len = dict()
extract_len['09'] = (2, 'ORA')
extract_len['49'] = (2, 'EOR')
extract_len['4A'] = (1, 'LSR')
extract_len['4C'] = (3, 'JMP')
extract_len['60'] = (1, 'RTS')
extract_len['6C'] = (3, 'JMP')
extract_len['85'] = (2, 'STA')
extract_len['86'] = (2, 'STX')
extract_len['8D'] = (3, 'STA')
extract_len['A9'] = (2, 'LDA')
extract_len['AD'] = (3, 'LDA')
extract_len['C9'] = (2, 'CMP')
extract_len['D0'] = (2, 'BNE')

pc = 0

start_time = time.clock()

while pc < len(code):
    try:
        opcode = code[pc]
        # Need to check if the opcode has been referenced
        if opcode in extract_len:
            length_to_extract = extract_len[opcode][0]
            instruction = extract_len[opcode][1]
            # OR UNPACKING (Tuple Assignment)
            (length_to_extract, instruction) = extract_len[opcode]
            # OR (Brackets not needed)
            length_to_extract, instruction = extract_len[opcode]

            # print(opcode, 'exist with len of', length_to_extract)
            # How many bytes to extract?
            if length_to_extract == 3:
                low_part, high_part = code[pc + 1:pc + length_to_extract]
                # Update here to get only one byte, not a list
                # extracted_part = high_part + low_part
                extracted_part = [high_part] + [low_part]
            elif length_to_extract == 2:
                extracted_part = code[pc + 1:pc + length_to_extract]
            else:
                print('extract current byte, pc={} - length_to_extract={}'.format(pc, length_to_extract))
                extracted_part = code[pc:pc + length_to_extract]
                extracted_part = instruction
                instruction = '   '
            print('  ', instruction, '-->', extracted_part)
            pc += length_to_extract
        else:
            # We cannot find the opcode, so it should be
            # an byte, asc,...
            print('   HEX', code[pc])
            pc += 1
    except:
        print('end of code')

# time.sleep(2)
end_time = time.clock()

print("That took {0:.4f} seconds to disasemble.".format(end_time - start_time))
