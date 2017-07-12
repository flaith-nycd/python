from sys import argv, exit


def dump_at_ts(option):
    if len(option) > 0:
        diskfile = option[0]
        track = option[1] if option[1:] else 0x11
        sector = option[2] if option[2:] else 0x00
        size = option[3] if option[3:] else 16
    else:
        print('Missing arguments')
        exit()

    print('Diskfile:', diskfile)
    print('Track:', track)
    print('Sector:', sector)
    print('Size:', size)


if __name__ == "__main__":
    dump_at_ts(argv[1:])
