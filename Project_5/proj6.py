'''
Alex Giacobbi
agiacobbi
Project 6: Generating random unigrams
25 October 2018
'''

import nltk
from nltk.corpus import brown
import re
import random

'''
Tokenizes section of the Brown corpus and returns a list of tokenized sentences
Pre: none
Post: returns list of lists where each sublist is a sentence containing ascii
encoded strings that are lowercase
'''
def tokenize():
    sents = brown.sents(categories='editorial')
    ascii = [[item.encode('ascii').lower() for item in lst] for lst in sents]

    for sent in ascii:
        for word in sent:
            #remove .,?():;"
            boo = True

    return ascii

'''
Creates dictionary of cumulative probabilities for each word where the word is
the key and the value is its cumulative probability
Pre: lst is a list of lists containing tokenized words
Post: Calculates relative frequency and cumulative probability by counting and
returns a dictionary of words and their cumulative probabilities
'''
def countFrequencies(lst):
    freqDict = {}
    numWords = 0.0
    cumProb = 0.0

    #counts frequency of wach word
    for sent in lst:
        for word in sent:
            if word not in ['.', ',', '?', '(', ')', ':', ';', '"', '!', "''"]:
                numWords += 1.0
                if word in freqDict:
                    freqDict[word] = freqDict[word] + 1.0
                else:
                    freqDict[word] = 1.0

    #calulates relative frequency for each word
    for item in freqDict:
        freqDict[item] = (freqDict[item] / numWords)

    #calculates cumulative probability for each word
    for item in freqDict:
        cumProb += freqDict[item]
        freqDict[item] = cumProb

    return freqDict

'''
Generates a sentence using the Bogensberger-Johnson technique outlined in specs
Pre: probDict contains words and cumulative probabilities
Post: prints a sentence by randomly selecting words from the dictionary using
B-J Technique mentioned above
'''
def generateSentence(probDict):
    rand = random.random()
    sent = ''

    for i in range(10):
        for item in probDict:
            if probDict[item] > rand:
                if i == 0:
                    sent += item.capitalize() + ' '
                elif i == 9:
                    sent += item + '.'
                else:
                    sent += item + ' '
                rand = random.random()
                break


    print '\n', sent, '\n'

def main():
    sentList= tokenize()
    freqDict = countFrequencies(sentList)
    for i in range(5):
        generateSentence(freqDict)    

main()
