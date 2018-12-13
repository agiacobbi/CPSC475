'''
Alex Giacobbi
agiacobbi
Test3C CYK Parser
13 December 2018
'''

import sys
import numpy

def getWords(fileName):
    return [word for line in open(fileName, 'r') for word in line.split()]

def getGrammar(fileName):
    theGrammar = {}

    for line in open(fileName, 'r'):
        rule = line.split()
        key = rule[0]
        value = []

        if key in theGrammar:
            if '|' in rule:
                for i in range(1, len(rule), 2):
                    theGrammar[key].append(rule[i])
            else:
                theGrammar[key].append(''.join(rule[1:]))
        else:
            if '|' in rule:
                theGrammar[key] = [rule[1]]
                for i in range(3, len(rule), 2):
                    theGrammar[key].append(rule[i])
            else:
                theGrammar[key] = [''.join(rule[1:])]

    return theGrammar

def findInGrammar(target, grammar):
    matches = []

    for item in target:
        for key in grammar:
            if item in grammar[key]:
                if key not in matches:
                    matches.append(key)

    return matches

def cartesianProduct(listA, listB):
    product = []

    for item in listA:
        for word in listB:
            product.append(''.join([item, word]))
    return product

def cykParse(words, grammar):
    n = len(words) + 1
    table = numpy.empty((n,n), dtype=list)

    for j in range(1, n):
        table[j - 1, j] = findInGrammar([words[j - 1]], grammar)
        for i in range(j - 2, -1, -1):
            targets = []
            for k in range(i + 1, j):
                product = cartesianProduct(table[i, k], table[k, j])
                for item in product:
                    if item not in targets:
                        targets.append(item)

                
            table[i, j] = findInGrammar(targets, grammar)

    if 'S' in table[0, n - 1]:
        return True
    return False


def main():
    grammarFile = sys.argv[1]
    stringFile = sys.argv[2]

    sentence = getWords(stringFile)
    grammar = getGrammar(grammarFile)

    if cykParse(sentence, grammar):
        print '\n', stringFile, 'is part of the grammar', grammarFile, '\n'
    else:
        print '\n', stringFile, 'is not part of the grammar', grammarFile, '\n'

main()
