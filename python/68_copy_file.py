# write a program to copy given file into another file 
#task use try except block in it.
import shutil
import os 
source = input("Enter source file ")
destination = input("Enter destination file")
if os.path.exists(source) == True:
    print("source file found ")
    if os.path.exists(destination) == False:
        shutil.copy(source,destination)
        print("file copied successfully")
    else:
        print(f"{destination} file already exists")
else:
    print(f"{source} not found")