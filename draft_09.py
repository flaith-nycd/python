import random
import string

# http://spyhce.com/blog/understanding-new-and-init

# http://agiliq.com/blog/2012/06/__new__-python/
import datetime


class A(object):
    def __new__(cls, *args, **kwargs):
        new_instance = object.__new__(cls, *args, **kwargs)
        setattr(new_instance, 'created_at', datetime.datetime.now())
        return new_instance

    def __init__(self, a, b):
        print("inside init")
        self.a, self.b = a, b


# obj1 = A(1, 2)

# https://concentricsky.com/articles/detail/pythons-hidden-new
class NewedBaseCheck(object):
    def __new__(cls, x):
        obj = super(NewedBaseCheck, cls).__new__(cls)
        obj._from_base_class = type(obj) == NewedBaseCheck
        return obj

    def __init__(self, x):
        print("inside init")
        self.x = x


# newed = NewedBaseCheck(5)
# print(newed.x)
class ProdosConst:
    FILE_TYPE = {
        0x00: 'NON',  # Typeless file
        0x01: 'BAD',  # Bad block(s) file
        0x04: 'TXT',  # Text file (ASCII text, msb off)
        0x06: 'BIN',  # Binary file (8-bit binary image)
        0x08: 'FOT',  # Graphics screen file
        0x0F: 'DIR',  # Directory file
        0x19: 'ADB',  # AppleWorks data base file
        0x1A: 'AWP',  # AppleWorks word processing file
        0x1B: 'ASP',  # AppleWorks spreadsheet file
        0xEF: 'PAS',  # ProDOS PASCAL file
        0xF0: 'CMD',  # ProDOS added command file
        0xF1: '$F1',  # User defined file types 1 through 8
        0xF2: '$F2',
        0xF3: '$F3',
        0xF4: '$F4',
        0xF5: '$F5',
        0xF6: '$F6',
        0xF7: '$F7',
        0xF8: '$F8',
        0xF9: 'OS',  # ProDOS Reserved
        0xFA: 'INT',  # Integer BASIC program file
        0xFB: 'IVR',  # Integer BASIC variable file
        0xFC: 'BAS',  # Applesoft BASIC program file
        0xFD: 'VAR',  # Applesoft stored variables file
        0xFE: 'REL',  # Relocatable object module file (EDASM)
        0xFF: 'SYS'  # ProDOS system file}
    }


def get_file_type(file_type):
    # if any(ProdosConst.FILE_TYPE[file_type]):
    if file_type in ProdosConst.FILE_TYPE.keys():
        return ProdosConst.FILE_TYPE[file_type]
    else:
        return '${:02X}'.format(file_type)


class StructFileProperty:
    # Structure of one File/Directory
    file_count = 0

    def __init__(self, st, nl, fn, pw):
        self.StorageType = st
        self.NameLength = nl
        self.FileName = fn
        self.Password = pw
        StructFileProperty.file_count += 1


class LoadDisk:
    listfiles = list()

    # HERE we're using __new__ because we need to return a value (here the list)
    # With __init__ you're always return None
    # def __new__(cls, *args, **kwargs):
    def __new__(cls, disk_name):
        obj = super(LoadDisk, cls).__new__(cls)
        obj._from_base_class = type(obj) == LoadDisk
        return obj

    def __init__(self, disk_name):
        """
        Here we will load the disk and after we will put all the files accordingly to the
        StructFileProperty
        And we will be able to print and get all the info we need in
        the _files list.

        :param disk_name:
        """

        # Add the disk name at the first position
        self.listfiles.append(StructFileProperty(0xFFFF, len(disk_name), disk_name, disk_name))

        # Now add 10 random files
        for i in range(10):
            # Generate a random word from 6 to 15 chars
            N = random.randrange(6, 15)
            random_name = ''.join(random.choice(string.ascii_uppercase) for _ in range(N))

            # Just a test to generate a password
            # https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python/23728630#23728630
            N = random.randrange(6, 12)
            password = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase +
                                                            string.digits) for _ in range(N))

            # Add in our list
            N = random.randrange(0x01, 0xFF)
            self.listfiles.append(StructFileProperty(N, len(random_name), random_name, password))


files = LoadDisk('TEST.DSK')

print('Disk name: {}'.format(files.listfiles[0].FileName))

for one_file in files.listfiles:
    if one_file.StorageType != 0xffff:
        # print('{} {:15} {:3d} {}'.format(
        #     get_file_type(one_file.StorageType), one_file.FileName, one_file.NameLength, one_file.Password)
        # )

        # Only with python 3 we can use 'f'
        print(
            f'{get_file_type(one_file.StorageType)} {one_file.FileName:15} {one_file.NameLength:3d} {one_file.Password}'
        )
