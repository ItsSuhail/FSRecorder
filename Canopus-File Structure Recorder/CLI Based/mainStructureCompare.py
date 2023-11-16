import pickle

# Encoding
def encode(l):
    fStr = ""
    for element in l:
        fStr = fStr + element + ":|:"
    
    fStr = fStr[:len(fStr) - 3]
    return fStr

# Function which compares the two structures
def _compare(newStructure, prevStructure):
    newFiles = set()
    deletedFiles = set()

    for k in newStructure.keys():
        pval = []
        nval = newStructure[k].split(":|:")
        try:
            pval = prevStructure[k].split(":|:")
        except KeyError: # When theres no key
            newFiles.add(str({k:encode(nval)}))
            continue


        # print(pval, nval)

        for e1 in pval:
            try:
                i1 = nval.index(e1)
                pass
            except ValueError:
                deletedFiles.add(str({k:e1}))

        
        for e2 in nval:
            try:
                i2 = pval.index(e2)
            except ValueError:
                newFiles.add(str({k:e2}))

    for j in prevStructure.keys():
        pval = prevStructure[j].split(":|:")
        nval = []
        try:
            nval = newStructure[j].split(":|:")
        except KeyError: # When theres no key
            deletedFiles.add(str({j:encode(pval)}))
            continue
        

        # print(pval, nval)

        for e11 in pval:
            try:
                i11 = nval.index(e11)
                pass
            except ValueError:
                deletedFiles.add(str({j:e11}))

        
        for e22 in nval:
            try:
                i22 = pval.index(e22)
            except ValueError:
                newFiles.add(str({j:e22}))

    return newFiles, deletedFiles


# deletedFiles = eval(deletedFiles)

# print(newFilesDict, deletedFilesDict)

def COMPARE(prevStructure, newStructure):
    try:
        loadedNStructure = pickle.load(open(newStructure, 'rb'))
        loadedPStructure = pickle.load(open(prevStructure, 'rb'))

        newFilesDict = {}
        deletedFilesDict = {}
        filesCreated, filesDeleted = _compare(loadedNStructure, loadedPStructure)
        for nF in filesCreated:
            newFilesDict.update(eval(nF))
            
        for dF in filesDeleted:
            deletedFilesDict.update(eval(dF))

        return newFilesDict, deletedFilesDict
    except Exception as error:
        print("An error occuered:", error)
        exit(-1)