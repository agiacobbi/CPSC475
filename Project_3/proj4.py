'''
Alex Giacobbi
agiacobbi
Project 4: Implementation of the soundex algorithm for a command line arg
           computer-science-> python proj4.py Jurafsky
26 September 2018
'''

import sys

'''
Removes all punctuation and spaces turns all letters lowercase
Pre stringIn is a string
Post returns a string of lowercase letters
'''
def cleanString(stringIn):
    cleanInput = ''

    for char in stringIn:
        if (char.isalpha()):
            cleanInput += char.lower()

    return cleanInput

'''
Removes characters as specified in step 1 keeping the first char
Pre stringIn is a string
Post returns a string with bad characters removed
'''
def stepOne(stringIn):
    soundex = stringIn[0]
    badChars = ('a', 'e', 'h', 'i', 'o', 'u', 'w', 'y')

    for char in stringIn[1:]:
        if (char not in badChars):
            soundex += char

    return soundex 

'''
Removes all remaining characters with a number as specified in step 2
Pre stringIn is a string
Post returns a string of one character followed by numbers
'''
def stepTwo(stringIn):
    soundex = stringIn[0]
    numberDict = {('b', 'f', 'p', 'v'): '1', ('c', 'g', 'j', 'k', 'q', 's', 'x', 
                 'z'): '2', ('d', 't'): '3', ('l'): '4', ('m', 'n'): '5', ('r'):
                 '6'}

    for char in stringIn[1:]:
        for group in numberDict:
            if char in group:
                soundex += numberDict[group]

    return soundex

'''
Removes all adjacent duplicate numbers as specified in step three
Pre stringIn is a string
Post returns a string of on letter followed by numbers without adjacent 
duplicates
'''
def stepThree(stringIn):
    if len(stringIn) == 0 or len(stringIn) == 1:
        return stringIn
    if stringIn[0] == stringIn[1]:
        return stepThree(stringIn[1:])
    
    return stringIn[0] + stepThree(stringIn[1:])

'''
Adds trailing zeros and returns final soundex string
Pre stringIn is a string
Post returns a string of one letter followed by 3 numbers with trailing zeros so 
that 4 characters are returned each time i.e. 'A420'
'''
def stepFour(stringIn):
    soundex = stringIn.upper() + '000'

    return soundex[0:4]

'''
Calls all steps in soundex algorithm for a string
Pre stringIn is a string
Post returns the soundex string of 4 characters
'''
def soundex(stringIn):
    stringIn = cleanString(stringIn)
    stringIn = stepOne(stringIn)
    stringIn = stepTwo(stringIn)
    stringIn = stepThree(stringIn)
    stringIn = stepFour(stringIn)

    return stringIn

def main():
    soundexName = soundex(sys.argv[1])
    print sys.argv[1], "->", soundexName

main()

