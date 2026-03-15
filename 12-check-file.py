#!/usr/bin/python3
import os

path = '/tmp/testfile.txt'

if os.path.isdir(path):
    print("It's a directory")
elif os.path.isfile(path):
    print("It's a file")
else:
    print("file or dir doesn't exists")
