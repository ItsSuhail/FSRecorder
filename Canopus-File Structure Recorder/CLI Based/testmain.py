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
* Ex- C:\\Users\\Suhail\\Desktop\\Project\\main.py [root is "C:\\"]
"""
import os

def get_files(directory):
    all_files = []
    
    for root, dirs, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            all_files.append(filepath)

    return all_files

print(get_files("C:\\Users\\Suhail Hasan Kg\\Desktop"))