import random
import string


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


print(get_file_type(0xFF))
print(get_file_type(0xAA))


# class SMSStore(object):
#     def __init__(self):
#         self.messages = []
#
#     def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
#         self.messages.append((False, from_number, time_arrived, text_of_SMS))
#
#     def message_count(self):
#         return len(self.messages)
#
#
# my_inbox = SMSStore()
# my_inbox.add_new_arrival('01234', '9:37 AM', 'How are you?')
# my_inbox.add_new_arrival('12340', '19:37 AM', 'Fine')
#
# print(my_inbox.messages[0])
# print(my_inbox.messages[1])

# Does not work
# PO_LOGICAL_ORDER = [(x, y)
#                     for x in [0x00, 0x0d, 0x0b, 0x09, 0x07, 0x05, 0x03, 0x01]
#                     for y in [0x0e, 0x0c, 0x0a, 0x08, 0x06, 0x04, 0x02, 0x0f]]
# print(PO_LOGICAL_ORDER)


# class StructFileProperty(object):
#     def __init__(self):
#         self.property = list()
#
#     def add_info_file(self, st, nl, fn):
#         self.property.append((st, nl, fn))
#
#     def message_count(self):
#         return len(self.property)
#
#
# one_file = StructFileProperty()
# one_file.add_info_file(0x0f, 5, 'TEST1')
# one_file.add_info_file(0x11, 6, 'TEST_2')
# one_file.add_info_file(0xF4, 7, 'TEST__3')
#
# print(one_file.property[0])
# print(one_file.property[1][2])


class StructFileProperty:
    # Structure of one File/Directory
    file_count = 0

    def __init__(self, st, nl, fn, pw):
        self.StorageType = st
        self.NameLength = nl
        self.FileName = fn
        self.Password = pw
        StructFileProperty.file_count += 1

    @classmethod
    def get_file_count(cls):
        return cls.file_count


# one_file = list()
# one_file.append(StructFileProperty(0x0f, 5, 'TEST1'))
# one_file.append(StructFileProperty(0x11, 6, 'TEST_2'))
# one_file.append(StructFileProperty(0xF4, 7, 'TEST__3'))
#
# print(len(one_file))
# print(one_file[0].FileName)
# print(one_file[1].FileName, one_file[1].NameLength)
# print(StructFileProperty.get_file_count())


class LoadDisk:
    _files = list()

    # def __init__(self, filename_disk):
    # HERE we're using __new__ because need to return a value (here the list)
    # With __init__ you're always return None
    # def __new__(cls, *args, **kwargs):
    def __new__(cls, filename_disk):
        """
        Here we will load the disk and after we will put all the files accordingly to the
        StructFileProperty
        And we will be able to print and get all the info we need in
        the _files list.

        :param filename_disk:
        """

        LoadDisk._files.append(StructFileProperty(0xFFFF, len(filename_disk), filename_disk, filename_disk))

        # A try with 10 files
        for i in range(10):
            # Generate a random word
            N = random.randrange(6, 15)
            random_name = ''.join(random.choice(string.ascii_uppercase) for _ in range(N))

            # Just a test to generate a password
            # https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python/23728630#23728630
            N = random.randrange(6, 12)
            password = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase +
                                                            string.digits) for _ in range(N))

            # Add in our list
            LoadDisk._files.append(StructFileProperty(0x0F, len(random_name), random_name, password))

        return LoadDisk._files


files = LoadDisk('TEST.DSK')

for one_file in files:
    print(one_file.StorageType, one_file.FileName, one_file.NameLength, one_file.Password)
