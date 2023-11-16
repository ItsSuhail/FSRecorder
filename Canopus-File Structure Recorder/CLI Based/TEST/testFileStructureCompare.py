import pickle

# Encoding
def encode(l):
    fStr = ""
    for element in l:
        fStr = fStr + element + ":|:"
    
    fStr = fStr[:len(fStr) - 3]
    return fStr

# Test for checking for change in the structure
# prevStructure = {'F:\\FSRecorder\\Canopus-File Structure Recorder\\CLI Based': 'testmain.py:|:something.py', 'x':'y'}
# newStructure = {'F:\\FSRecorder\\Canopus-File Structure Recorder\\CLI Based': 'testmain.py:|:en.py',"m":"N"}

prevStructure = pickle.load(open('1', 'rb'))
newStructure = pickle.load(open('2', 'rb'))



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



newFilesDict = {}
deletedFilesDict = {}
for nF in newFiles:
    newFilesDict.update(eval(nF))
    
for dF in deletedFiles:
    deletedFilesDict.update(eval(dF))


# deletedFiles = eval(deletedFiles)

print(newFilesDict, deletedFilesDict)
