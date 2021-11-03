import sys

argv = sys.argv
argv.pop(0)

for arg in argv:
    print(arg, end=' ')

# python 3.5.2.py arg1 arg2