'''
Alex Giacobbi
agiacobbi
Test2a: Implementing the forward algorithm
15 November 2018
'''

import numpy
import csv
import sys

'''
Gets matrix from csv file and stores in a nummpy array
Returns the array
'''
def readMatrixFromFile(inFile):
    reader = csv.reader(open(inFile, 'r'), delimiter=',')
    valList = list(reader)
    matrix = numpy.array(valList).astype('float')

    return matrix

'''
Gets string containing sequence of operations
Returns a list of integers
'''
def makeObservationSequence(stringIn):
    return [int(num) for num in stringIn]

'''
Uses HMM defined by aMatrix and bMatrix to calculate the likelihood of an
observation sequence obsSeq
Pre: obsSeq is a list of observations
Post: fills the forward trellis using the forward algorithm and returns the 
      likelihood
'''
def forward(obsSeq, aMatrix, bMatrix):
    t = len(obsSeq)     #length of observation sequence
    n = len(aMatrix)    #number of states including start and end
    likelihood = 0.0
    probMat = numpy.zeros((n, t))

    for state in range(1, n - 1):
        probMat[state][0] = aMatrix[0][state] * bMatrix[state][obsSeq[0] - 1]

    for step in range(1, t):
        for state in range(1, n - 1):
            probSum = 0.0
            for prev in range(n):
                probSum += (probMat[prev][step - 1] * aMatrix[prev][state]
                            * bMatrix[state][obsSeq[step] - 1])
            probMat[state][step] = probSum

    for state in range(1, n - 1):
        likelihood += (probMat[state][t - 1] * aMatrix[state][n - 1])
    probMat[n - 1][t - 1] = likelihood

    return probMat[n - 1][t - 1]
    

def main():
    A_Matrix = readMatrixFromFile(sys.argv[1])
    B_Matrix = readMatrixFromFile(sys.argv[2])
    observation = makeObservationSequence(sys.argv[3])

    likelihood = forward(observation, A_Matrix, B_Matrix)

    print
    print "The likelihood of sequence", sys.argv[3], "is", likelihood
    print

main()
