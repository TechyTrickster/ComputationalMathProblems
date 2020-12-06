#!/usr/bin/python3

import sys

min = sys.maxsize
max = -sys.maxsize
total = 0
count = 0
for line in sys.stdin:
    values = line.split('\t')[1].split(',')
    (potentialMin, potentialMax, averageOfRun) = (int(values[0].replace('[', '')), int(values[1]), float(values[2].replace(']', '').rstrip()))
    total = total + averageOfRun
    count = count + 1
    if potentialMin > max:
        max = potentialMin
    if potentialMin < min:
        min = potentialMin
    if potentialMax > max:
        max = potentialMax
    if potentialMax < min:
        min = potentialMax
average = total / count
print(min, max, average, sep = '\t')
