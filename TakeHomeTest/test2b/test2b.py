'''
Alex Giacobbi
agiacobbi
Test2b: Implementing the Viterbi algorithm
29 November 2018
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
Uses HMM defined by aMatrix and bMatrix to calculate the most probable state
sequence given observation sequence obsSeq
Pre: obsSeq is a list of observations
Post: fills the Viterbi trellis using the Viterbi algorithm and returns the 
      most probable state sequence
'''
def Viterbi(obsSeq, aMatrix, bMatrix):
    t = len(obsSeq)     #length of observation sequence
    n = len(aMatrix)    #number of states including start and end
    maxProbability = 0.0
    backTrace = numpy.zeros((n, t), dtype=int)
    viterbi = numpy.zeros((n, t))
    stateSeq = []
    weather = []

    for state in range(1, n - 1):
        viterbi[state][0] = aMatrix[0][state] * bMatrix[state][obsSeq[0] - 1]

    for step in range(1, t):
        for state in range(1, n - 1):
            maxVal = 0.0
            for prev in range(n):
                maxVal = max(viterbi[prev][step - 1] * aMatrix[prev][state]
                             * bMatrix[state][obsSeq[step] - 1], maxVal)
                if (viterbi[prev][step - 1] * aMatrix[prev][state] 
                    * bMatrix[state][obsSeq[step] - 1] == maxVal):
                    backTrace[state][step] = prev

            viterbi[state][step] = maxVal

    for state in range(1, n - 1):
        maxProbability = max(viterbi[state][t - 1] * aMatrix[state][n - 1], 
                             maxProbability)

        if (viterbi[state][t - 1] * aMatrix[state][n - 1] == maxProbability):
            backTrace[n - 1][t - 1] = state

    viterbi[n - 1][t - 1] = maxProbability

    stateSeq.append(backTrace[n - 1][t - 1])
    for step in range(t - 1):
        stateSeq.append(backTrace[stateSeq[step]][t - step - 1])

    for step in range(t):
        if (stateSeq[t - step - 1] == 1):
            weather.append('C')
        else:
            weather.append('H')

    return weather

def main():
    A_Matrix = readMatrixFromFile(sys.argv[1])
    B_Matrix = readMatrixFromFile(sys.argv[2])
    observation = makeObservationSequence(sys.argv[3])

    weather = Viterbi(observation, A_Matrix, B_Matrix)
    sequence = ' '.join(str(x) for x in weather)

    print
    print "The most probable weather sequence is", sequence
    print

main()
