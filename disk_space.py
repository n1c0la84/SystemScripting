import os, collections
import ctypes, sys
import win32api

diskusage = collections.namedtuple('usage', 'totalbytes usedpercent freepercent')

def disk_usage(path):
    _, total, free = ctypes.c_ulonglong(), ctypes.c_ulonglong(), ctypes.c_ulonglong()
    if sys.version_info >= (3,) or isinstance(path, unicode):
        function = ctypes.windll.kernel32.GetDiskFreeSpaceExW
    else:
        function = ctypes.windll.kernel32.GetDiskFreeSpaceExA
    result = function(path, ctypes.byref(_), ctypes.byref(total), ctypes.byref(free))
    used = total.value - free.value
    usedpercent = used / total.value * 100
    freepercent = free.value / total.value * 100
    return diskusage(total.value, usedpercent, freepercent)

def bytes2human(n):
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i+1)*10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return "%sB" % n

if __name__ == '__main__':
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    del drives[-1]  #cdrom

    for drive in drives:
        print(drive)
        print(disk_usage(drive))