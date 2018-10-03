'''
Alex Giacobbi
agiacobbi
Project 5: Implementation of minimum edit distance algorithm
4 October 2018
'''

import sys
import numpy

def minimumEditDistance(target, source):
    n = len(target)
    m = len(source)
    dist = numpy.zeros((n + 1, m + 1), dtype=int)

    dist[0, 0] = 0

    for i in range(1, n + 1):
        dist[i, 0] = dist[i - 1, 0] + 1
    for j in range(1, m + 1):
        dist[0, j] = dist[0, j - 1] + 1

    for col in range(1, n + 1):
        for row in range(1, m + 1):
            dist[col, row] += min(dist[col - 1, row] + 1, 
                              dist[col - 1, row - 1] + 
                              subCost(target[col - 1], source[row - 1]),
                              dist[col, row - 1] + 1)
    
    print dist
    return dist[n, m]

def subCost(charA, charB):
    if (charA == charB):
        return 0
    else:
        return 2

def main():
    print minimumEditDistance(sys.argv[1], sys.argv[2])

main()
