from nltk.corpus import inaugural
import re
import pickle

'''
Tokenizes words in an inaugural address, removes extraneous characters
Takes an inaugural address from inaugural corpus
Returns a list of words in the address
'''
def tokenizeAddress(address):
    inauguralAddress = inaugural.raw(address)
    regex = r'\w+'
    tokenizedList = re.findall(regex, inauguralAddress)
    return tokenizedList

'''
Compiles each address into a large list of lists
For each file, appends tokenized Address to list
Returns master list of each tokenized address
'''
def writeList():
    masterList = []
    for file_id in inaugural.fileids():
        masterList.append(tokenizeAddress(file_id))
    return masterList

'''
Serializes list of addresses using pickle
Takes a list and writes to proj3.pkl
'''
def pickler(pickleList):    
    fout = open ('proj3.pkl','wb')
    pickle.dump(pickleList,fout)

    fout.close()

def main():
    pickler(writeList())

main()

