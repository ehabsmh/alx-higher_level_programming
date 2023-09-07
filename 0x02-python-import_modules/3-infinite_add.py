#!/usr/bin/python3
import sys

args = sys.argv
args_len = len(args)
result = 0

for i in range(1, args_len):
    result += int(args[i])

print(result)
