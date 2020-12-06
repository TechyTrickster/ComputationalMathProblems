#!/usr/bin/python3

import sys
import random
import numpy as np
np.set_printoptions(suppress=True)

equations = int(sys.argv[1])
for index in range(0,equations):
    width = random.randint(3, 30)
    lowerBound = random.randint(-999999, 1)
    upperBound = random.randint(9, 999999)
    poly = np.random.uniform(low = -9999, high = 9999, size = (width,))
    polyStr = np.array2string(poly, separator = ',').replace(' ', '').replace('[', '').replace(']', '').strip().replace('\n', '')
    data = polyStr + ":" + str((lowerBound, upperBound))
    print(index, data, sep = '\t')
