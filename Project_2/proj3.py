import matplotlib.pyplot as plt
import pickle
from nltk.corpus import inaugural

'''
Deserializes pickled list using pickle
Opens proj3.pkl, depickles and reads into a list
Returns deserialized list
'''
def depickler():
    fin = open('proj3.pkl', 'rb')
    listsIn = pickle.load(fin)

    fin.close()

    return listsIn

'''
Gets list of years to be displayed on x-axis
Returns list of years
'''
def yearList():
    yearList = []
    for file_id in inaugural.fileids():
        yearList.append(file_id.split('-')[0])
    return yearList

'''
Gets a word from user to check frequency of
Returns string word
'''
def getWord():
    print("Note: Be sure to put quotation marks around the input")
    word = input("Enter a word to see frequency-> ")

    return word

'''
Counts frequency of wordIn in each list in listIn
wordIn is a string and listIn is a list of lists
Returns a dictionary where the key is an inaugural address index and the value 
is the number of times wordIn appears in the address
'''
def freq_table(wordIn, listIn):
    count_dict = {}
    for address in listIn:
        count_dict[listIn.index(address)] = 0
        for word in address:
            if (word == wordIn):
                count_dict[listIn.index(address)] += 1

    return count_dict

'''
Plots frequency of word appearence for each inaugural address
frequencyDict is dictionary of addresses and frquencies to be plotted
Plot is displayed with address index on the x-axis and frequency on the y-axis
'''
def plotFrequency(frequencyDict, yearList):
    x = [year for year in yearList]
    y = [frequencyDict[address] for address in frequencyDict]
    plt.plot(x,y)
    plt.show()

def main():
    listIn = depickler()
    searchWord = getWord()
    freqDict = freq_table(searchWord, listIn)
    years = yearList()
    plotFrequency(freqDict, years)

main()
