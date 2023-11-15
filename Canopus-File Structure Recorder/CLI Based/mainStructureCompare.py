import pickle

def COMPARE(prevStructure, newStructure):
    try:
        # Encoding
        def encode(l):
            fStr = ""
            for element in l:
                fStr = fStr + element + ":|:"
            
            fStr = fStr[:len(fStr) - 3]
            return fStr
        
        
        prevStructure = pickle.load(open(prevStructure, 'rb'))
        newStructure = pickle.load(open(newStructure, 'rb'))

        newFiles = set()
        deletedFiles = set()
        for i in newStructure.keys():
            pval = []
            nval = newStructure[i].split(":|:")
            try:
                pval = prevStructure[i].split(":|:")
            except KeyError: # When theres no key
                newFiles.add(str({i:encode(nval)}))
                continue


            # print(pval, nval)

            for e1 in pval:
                try:
                    index1 = nval.index(e1)
                    pass
                except ValueError:
                    deletedFiles.add(str({i:e1}))

            
            for e2 in nval:
                try:
                    index2 = pval.index(e2)
                except ValueError:
                    newFiles.add(str({i:e2}))

        for j in prevStructure.keys():
            pval = prevStructure[j].split(":|:")
            nval = []
            try:
                nval = newStructure[j].split(":|:")
            except KeyError: # When theres no key
                deletedFiles.add(str({j:encode(pval)}))
                continue
            

            # print(pval, nval)

            for e21 in pval:
                try:
                    index21 = nval.index(e21)
                    pass
                except ValueError:
                    deletedFiles.add(str({j:e21}))

            
            for e22 in nval:
                try:
                    index22 = pval.index(e22)
                except ValueError:
                    newFiles.add(str({j:e22}))



        newFilesDict = {}
        deletedFilesDict = {}
        for nF in newFiles:
            newFilesDict.update(eval(nF))
            
        for dF in deletedFiles:
            deletedFilesDict.update(eval(dF))

        return newFilesDict, deletedFilesDict
    except Exception as error:
        print(f"An error occured: {error}")
        exit(-1)