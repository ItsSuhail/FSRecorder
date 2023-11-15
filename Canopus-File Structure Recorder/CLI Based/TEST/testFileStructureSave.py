import pickle
import os

def get_files(directory):
    all_files = []
    all_roots = []
    
    for root, dirs, files in os.walk(directory):
        for filename in files:
            # print(root)
            # filepath = os.path.join(filename)
            all_files.append(filename)
            all_roots.append(root)

    return all_files, all_roots

x,y = get_files("F:\\FSRecorder\\Canopus-File Structure Recorder\\CLI Based")


# Classifying Test
def classify(l1, l2):
    final_dict = {}
    n = 0
    for e in l2:
        try:
            data = final_dict[e]
            final_dict.update({e:(data + ":|:" + l1[n])})
        except KeyError:
            final_dict.update({e:(l1[n])})
        n+=1
    
    return final_dict

fDict = classify(x,y)

iFName = input("Filename: ")


def pickleData(data, name):
    dFile = open(f"{name}", 'ab')
    pickle.dump(data, dFile)
    dFile.close()

pickleData(fDict, iFName)