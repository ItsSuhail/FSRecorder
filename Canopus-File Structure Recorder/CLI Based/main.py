import os
import mainStructureRecord
import mainStructureCompare


if __name__ == "__main__":
    while(True):
        print("1* Record a file structure: \n2* Compare two files structures: \n3* EXIT: \n\n")
        inp = -1
        try:
            inp = int(input("> "))
        except Exception:
            print("\n\n\n")
            continue;

        if(inp == -1):
            print("\n\n\n")
            continue;
        elif(inp == 1):
            filepath = input("Enter the path of the structure: ")
            if(os.path.isdir(filepath)):
                recordName = input("Name of the recording (optional): ")
                if(recordName.strip() != ''):
                    status = mainStructureRecord.RECORD(filepath, recordName)    
                else:
                    status = mainStructureRecord.RECORD(filepath)
                
                if(status!=None):
                    print(f"\n\nAn error occured: {status}")
                    exit()
                    
                print("\n\nStructure recorded successfully.\n\n\n")
            else:
                print("\n\nPlease provide valid path.\n\n\n")
            continue

        elif(inp == 2):
            oldStructure = input("Enter the path of record of old structure: ")
            newStructure = input("Enter the path of record of latest structure: ")
            if(os.path.isfile(oldStructure) and os.path.isfile(newStructure)):
                newDict, deletedDict = mainStructureCompare.COMPARE(oldStructure, newStructure)

                print("\n\nThe new files created are: ", newDict, "\n")
                print("The old files deleted are: ", deletedDict, "\n")
                print("\n\n\n")
            
            else:
                print("Please provide valid path(s).\n\n\n")
            
            continue;
            
        elif(inp == 3):
            print("\n\n\n\n")
            exit(0)

        else:
            print("\n\n\n")
            continue;