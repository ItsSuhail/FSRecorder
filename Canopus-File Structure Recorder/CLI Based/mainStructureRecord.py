import pickle
import os
import datetime

def RECORD(directory, name=datetime.datetime.now().strftime("%H-%M-%S--%Y-%m-%d")):
    name = name + ".cfsr"
    try:
        # Getting all the files with the root in the directory
        allFiles = []
        allRoots = []
        
        for root, dirs, files in os.walk(directory):
            for filename in files:
                allFiles.append(filename)
                allRoots.append(root)


        # Classifying the files based on common root (if any)
        
        finalDict = {}
        n = 0
        for e in allRoots:
            try:
                data = finalDict[e]
                finalDict.update({e:(data + ":|:" + allFiles[n])})
            except KeyError:
                finalDict.update({e:(allFiles[n])})
            n+=1
        

        # Recording the structure
        dFile = open(f"{name}", 'ab')
        pickle.dump(finalDict, dFile)
        dFile.close()

        return None
    except Exception as error:
        return error