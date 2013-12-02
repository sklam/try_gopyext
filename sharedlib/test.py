from ctypes import *

lib = CDLL('./bar.so')
goadd = lib['example.main.Add']
print goadd
goadd.argtypes = c_int, c_int
goadd.restype = c_int
print goadd(1, 2)

