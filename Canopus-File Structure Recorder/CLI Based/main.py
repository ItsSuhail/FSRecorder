import os
import mainStructureRecord
import mainStructureCompare


if __name__ == "__main__":
    while(True):
        print("1* Record a file structure: \n2* Compare two files structures")
        inp = -1
        try:
            inp = int(input("> "))
        except Exception:
            print("\n\n\n")
            continue;

        if(inp == -1):
            print("n\n\n")
            continue;
        elif(inp == 1):
            filepath = input("Enter the path of the structure: ")
            if(os.path.isdir(filepath)):
                recordName = input("Name of the recording (optional): ")
                status = mainStructureRecord.RECORD(filepath, recordName)
                if(status!=None):
                    print(f"An error occured: {status}")
                    exit()
                
                print("Structure recorded successfully.\n\n\n")
            else:
                print("Please provide valid path.\n\n\n")
            continue

        elif(inp == 2):
            oldStructure = input("Enter the path of record of old structure: ")
            newStructure = input("Enter the path of record of latest structure: ")
            if(os.path.isfile(oldStructure) and os.path.isfile(newStructure)):
                newDict, deletedDict = mainStructureCompare.COMPARE(oldStructure, newStructure)

                print("The new files created are: ", newDict, "\n")
                print("The old files deleted are: ", deletedDict, "\n")
                print("\n\n\n")
            
            else:
                print("Please provide valid path(s).\n\n\n")
            
            continue;
            
        else:
            print("\n\n\n")
            continue;