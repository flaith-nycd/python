import os
from array import array


class DiskfileError(Exception):
    """Exception constructor"""

    def __init__(self, diskfile, message):
        self._diskfile = diskfile
        self._message = message

    # Will be used when an exception will occur
    def __str__(self):
        return "The disk file \"{}\" {} !".format(self._diskfile, self._message)


class Disk:
    def __init__(self, diskname):
        # Keep the name of our disk
        self._diskname = diskname

        # and init its size to 0
        self._disksize_raw = 0

        # Init memory for the disk
        # the size will be given by the disk size
        self._memdisk = array('B', [0x00] * 256)

    # Return the real size of the file
    # to be used with the _load method
    def _get_file_size(self):
        try:
            return os.stat(self._diskname).st_size
        except:
            raise DiskfileError(self._diskname, 'not found')

    # Load the disk file in the array
    def _load(self):
        with open(self._diskname, 'rb') as diskfile:
            # memdisk is an array, so we use array method 'fromfile'
            # to load and populate our array with the real size
            # of the file
            self._disksize_raw = self._get_file_size()
            self._memdisk.fromfile(diskfile, self._disksize_raw)

    def get_memory(self):
        return self._memdisk


class DiskDos33(Disk):
    def __init__(self, diskname):
        Disk.__init__(self, diskname)


d = DiskDos33('test')
print(d.get_memory())
print(d._memdisk.buffer_info())
