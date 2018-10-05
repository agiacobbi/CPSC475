'''
Alex Giacobbi
agiacobbi
Project 5: Implementation of minimum edit distance algorithm
4 October 2018
'''

import sys
import numpy

'''
Produces minimum edit distance matrix using algorithm outlined in textbook
Pre: source and target are strings to find minimum edit distance of
Post: returns a matrix with minimum edit distance stored in bottom right index
'''
def minimumEditDistance(source, target):
    n = len(target)
    m = len(source)
    dist = numpy.zeros((n + 1, m + 1), dtype=int)

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
    
    return dist

'''
Calculates substitution cost for two characters
Pre: charA and charB are characters
Post: returns 0 if the characters are the same, 2 otherwise
'''
def subCost(charA, charB):
    if (charA == charB):
        return 0
    else:
        return 2

'''
Prints alignment of the source and target using minimum edit distance matrix
Pre: source and target are strings and dist is a minimum edit distance matrix
Post: alignment of source and target is printed in form outlined in textbook
'''
def outputAlignment(source, target, dist):
    col = len(target)
    row = len(source)
    s = len(target) - 1
    t = len(source) - 1

    while (s >= 0 or t >= 0):
        if (dist[col, row] == dist[col - 1, row - 1] + subCost(target[col - 1], source[row - 1])):
            print source[s], target[t]
            col -= 1
            row -= 1
            t -= 1
            s -= 1
        elif (dist[col, row] == dist[col - 1, row] + 1):
            print '*', target[t]
            col -= 1            
            t -= 1
        elif (dist[col, row - 1] == dist[col, row] - 1):
            print source[s], '*'
            row -= 1
            s -= 1

    print

    return

def main():
    source = sys.argv[1]
    target = sys.argv[2]
    distanceMatrix = minimumEditDistance(source, target)
    print "\nMinimum edit distance:", distanceMatrix[len(source), len(target)], '\n'
    outputAlignment(source, target, distanceMatrix)

main()
