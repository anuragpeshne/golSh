#!/usr/bin/python

import sys
import fileinput
import random
import time

matrix = []
for line in fileinput.input():
    row = map(lambda x: int(x), line.rstrip())
    matrix.append(row)

if len(matrix) == 0:
    length, breath = random.randint(3, 10), random.randint(3, 10)
    for row in range(breath):
        row = []
        for col in range(length):
            row.append(random.randint(0, 1))
        matrix.append(row)

def generateNextGen(matrix):
    nMatrix = []
    for row in range(len(matrix)):
        nRow = []
        for col in range(len(matrix[0])):
            neighCount = getLiveNeighCnt(matrix, row, col)
            if matrix[row][col] == 1:
                if neighCount < 2:
                    nRow.append(0)
                elif (neighCount == 2) or (neighCount == 3):
                    nRow.append(1)
                else:        # neighCount > 3
                    nRow.append(0)
            else:
                if neighCount == 3:
                    nRow.append(1)
                else:
                    nRow.append(0)
        nMatrix.append(nRow)
    return nMatrix

def getLiveNeighCnt(matrix, row, col):
    count = 0
    for i in range(-1, 2, 1):
        count = count + getNeigh(matrix, row - 1, col + i)
        count = count + getNeigh(matrix, row + 1, col + i)

    count = count + getNeigh(matrix, row, col + 1)
    count = count + getNeigh(matrix, row, col - 1)
    return count

def getNeigh(matrix, row, col):
    try:
        return matrix[row][col]
    except IndexError:
        return 0

nMatrix = generateNextGen(matrix)
while (nMatrix != matrix):
    matrix = nMatrix
    nMatrix = generateNextGen(matrix)
    print reduce(
            lambda x, y : x + '\n' +  y,
            map(lambda a: reduce(lambda x, y: str(x) + str(y), a), matrix)
            )
    time.sleep(1)
