"""
# My Idea: 
+ We input the required directory to be recorded
+ Each element of the directry will be recorded
+ we'll save the recorded file and serialize it with pickle
+ we can see the differences between 2 recordings i.e. we can see the changes which occured


- Understand how the file system in python works
- Record every file structure in a list, then pickle the list
- When loaded any recorded structure, unpickle the data into a list

* I need to store each and everyfile with it's path stored along with the file name under the root given
* Ex- C:\\Users\\Suhail\\Desktop\\Project\\main.py [root is "C:\\Users\\Suhail\\Desktop\\Project"]
"""

# Test for Getting all the files

# import os

# def get_files(directory):
#     all_files = []
#     all_roots = []
    
#     for root, dirs, files in os.walk(directory):
#         for filename in files:
#             # print(root)
#             # filepath = os.path.join(filename)
#             all_files.append(filename)
#             all_roots.append(root)

#     return all_files, all_roots

# x,y = get_files("F:\\FSRecorder\\Canopus-File Structure Recorder\\CLI Based")


# # Classifying Test
# def classify(l1, l2):
#     final_dict = {}
#     n = 0
#     for e in l2:
#         try:
#             data = final_dict[e]
#             final_dict.update({e:(data + ":|:" + l1[n])})
#         except KeyError:
#             final_dict.update({e:(l1[n])})
#         n+=1
    
#     return final_dict

# print(classify(x,y))




# Encoding
def encode(l):
    fStr = ""
    for element in l:
        fStr = fStr + element + ":|:"
    
    fStr = fStr[:len(fStr) - 3]
    return fStr

# Test for checking for change in the structure
prevStructure = {'F:\\FSRecorder\\Canopus-File Structure Recorder\\CLI Based': 'testmain.py:|:something.py', 'x':'y'}
newStructure = {'F:\\FSRecorder\\Canopus-File Structure Recorder\\CLI Based': 'testmain.py:|:en.py',"m":"N"}


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



# newFilesDict = {}
# deletedFiles = eval(deletedFiles)

# print(newFiles, deletedFiles)