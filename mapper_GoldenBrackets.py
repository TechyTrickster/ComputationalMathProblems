#!/usr/bin/python3

import sys
import numpy as np
tolX = 0.0001
tolY = 0.0001

for line in sys.stdin:
    #break down the line taken from standard input so it can be processed by golden
    (index, data) = line.strip().split('\t')
    (polynomialRaw, boundRaw) = data.split(':')
    polyNumerical = list(map(float, polynomialRaw.split(',')))
    polynomial = np.array(polyNumerical.split(','))
    (lowerBoundOrig, upperBoundOrig) = boundRaw.split(',')
    upperBound = upperBoundOrig
    lowerBound = lowerBoundOrig

    #begin translation of books matlab version of golden to python, with better variable names
    ratio = (3 - math.sqrt(5)) / 2
    diffRatio = 1 - ratio
    newBoundLow = lowerBound + ratio * (upperBound - lowerBound)
    newBoundHigh= lowerBound + diffRatio * (upperBound - lowerBound)
    evalLow = np.polyval(polynomial, newBoundLow)
    evalHigh= np.polyval(polynomial, newBoundHigh)
    iterations = 0

    while (abs(upperBound - lowerBound) > tolX) or (abs(evalLow - evalHigh) > tolY):
        if(evalLow < evalHigh):
            upperBound = newBoundHigh
            newBoundHigh = newBoundLow
            newBoundLow = lowerBound + ratio * (upperBound - lowerBound)
            evalHigh = evalLow
            evalLow = np.polyval(polynomial, newBoundLow)
        else:
            lowerBound = newBoundLow
            newBoundLow = newBoundHigh
            newBoundHigh = lowerBound + diffRatio * (upperBound - lowerBound)
            evalLow = evalHigh
            evalHigh = np.polyval(polynomial, newBoundHigh)

        iterations = iterations + 1


    data = str(index) + ':' + polynomialRaw + ':' + str((lowerBound, upperBound)) + ':' + str((lowerBoundOrig, upperBoundOrig)) + ":" + str(evalLow)
    print(index, data, sep = '\t')
