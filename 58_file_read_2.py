#write a program to read data from file 
filename = input("Enter file name")
mode = "r" #r = read mode  
try:
    #open file 
    file = open(filename,mode)
    #read data from file (line by line)
    for line in file:
        print(line.strip())
    file.close()
except FileNotFoundError as error:
    print("file not found ")
else:
    print("_"*100)
    print("file read successfully")
finally:
    print('end of program')
