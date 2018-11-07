import pickle

def depickler():
    fin = open('proj7b.pkl', 'rb')
    probDict = pickle.load(fin)

    fin.close()
    return probDict



def main():
    probDict = depickler()

    print probDict[2]

main()
