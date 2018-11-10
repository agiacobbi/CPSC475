import pickle
import random
from itertools import islice

def depickler():
    fin = open('proj7b.pkl', 'rb')
    probDict = pickle.load(fin)

    fin.close()
    return probDict

'''
Generates a sentence using the Bogensberger-Johnson technique outlined in specs
Pre: probDict contains words and cumulative probabilities
Post: prints a sentence by randomly selecting words from the dictionary using
B-J Technique mentioned above
'''
def generateSentence(probDict, n):
    rand = random.random()
    sent = ''
    i = 0

    while i < (12 / n):
        for item in probDict:
            if (item[1] > rand):
                if i == 0:
                    sent += item[0].capitalize() + ' '
                elif i == (12 / n) - 1:
                    sent += item[0] + '.'
                else:
                    sent += item[0] + ' '
                rand = random.random()
                break
        i += 1

    print '\n', sent, '\n'

def main():
    probDict = depickler()

    generateSentence(probDict[0], 1)
    generateSentence(probDict[1], 2)
    generateSentence(probDict[2], 3)
    generateSentence(probDict[3], 4)

main()
