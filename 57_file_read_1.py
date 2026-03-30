#write a program to read data from file 
filename = "fruits.txt"
mode = "r" #r = read mode  

#open file 
file = open(filename,mode)
#read data from file (line by line)
for line in file:
    print(line.strip())

file.close()
print("_"*100)
print("file read successfully")
