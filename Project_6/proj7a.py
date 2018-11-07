import re
import pickle

def pickler(pickleDict):    
    fout = open('proj7b.pkl','wb')
    pickle.dump(pickleDict, fout)

    fout.close()

def tokenizeText(fileName):
    inputFile = open(fileName, 'r')
    sents = []

    for line in inputFile:
        words = []
        if (line != '\n'):
            words.append('<s>')
            for word in line.split():
                words.append(tokenizeWord(word))
            words.append('</s>')
        sents.append(words)

    return sents

def tokenizeWord(word):
    goodChars = [chr(value) for value in range(ord('a'), ord('z') + 1, 1)]
    goodChars.append('\'')
    token = ""

    word = word.lower()
    for char in word:
        if (char in goodChars):
            token = token + char

    return token

def makeProbabilityDict(sents, n):
    probDict = {}
    nList = ngrams(sents, n)
    numWords = float(len(nList))
    cumProb = 0.0

    for item in nList:
        word = ngramToString(item)
        if word in probDict:
            probDict[word] = probDict[word] + 1.0
        else:
            probDict[word] = 1.0

    for item in probDict:
        probDict[item] = (probDict[item] / numWords)
        cumProb += probDict[item]
        probDict[item] = cumProb

    return probDict 

def ngramToString(ngram):
    nString = ''

    for word in ngram:
        nString = nString + word + ' '

    return nString[:-1]

def ngrams(inList, n):
    if (n == 1):
        return inList

    output = []
    for sent in inList:
        for i in range(len(sent) - n + 1):
            output.append(sent[i: i + n])

    return output

def main():
    lines = tokenizeText('shakespeare.txt')
    probDict = {1:makeProbabilityDict(lines, 1), 
                2:makeProbabilityDict(lines, 2),
                3:makeProbabilityDict(lines, 3),
                4:makeProbabilityDict(lines, 4)}

    pickler(probDict)

main()


