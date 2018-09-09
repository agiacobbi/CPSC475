'''
Alex Giacobbi
agiacobbi
Project 2: Displays the number of instances of the substring in the file
7 September 2018
'''

'''
Iterates through substring checking if each character matches string. 
If substring exists within string, returns 1. Else returns 0
'''
def searchSub(string, subStr, posStr):
    posSub = 0
    while(posSub < len(subStr)):
        if string[posStr] == subStr[posSub]:
            posStr += 1
            posSub += 1
        else:
            return 0
    return 1

'''
Iterates though string calling searchSub for each character count increments for each substring subStr found
Returns number of substrings subStr found in string
'''
def countSubs(string, subStr):
    pos = 0
    count = 0
    while(pos <= len(string) - len(subStr)):
        count += searchSub(string, subStr, pos)
        pos +=1
    return count

'''
Accepts input to open file as specified by user. Handles error checking for invalid filenames
Returns opened file
'''
def goodOpen():
    print ("Note: Be sure to put quotation marks around the file name")
    while(True):
        fileIn = input("Enter an input file name\n")
        try:
            fileIn = open(fileIn, 'r')
            break
        except:
            print("Invalid file name. Try again.")
    return fileIn

'''
Reads file fileName to string
Returns string
'''
def readFile(fileName):
    string = fileName.read()
    return string

'''
Gets input from user
Returns substring subStr
'''
def getSub():
    print("Note: Be sure to put quotation marks around the input")
    subStr = input("Enter a substring to search for\n")
    return subStr

def main():
    fin = goodOpen()
    subStr = getSub()
    string = readFile(fin)

    print(countSubs(string, subStr))

main()