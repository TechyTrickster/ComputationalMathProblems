#!/usr/bin/python3
import sys
import math

min = sys.maxsize
max = -sys.maxsize
count = 0
total = 0
for line in sys.stdin:
    value = int(line)
    total = total + value
    count = count + 1
    if value > max:
        max = value
    if value < min:
        min = value

avg = total / count
print(1, [min, max, avg], sep = '\t')
