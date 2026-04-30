#write a program to read given file which has numbers. if number is odd, write it into odd.txt file otherwise write it into even.txt file 
#1st read content from file
try:
    filename = input("Enter file name to read numbers from it ")
    filename2 = "odd.txt"
    filename3 = "even.txt"
    mode = 'r'
    with open(filename,mode) as file1:
        #open other two files in write mode
        odd = open(filename2,"w")
        even = open(filename3,"w")
        for line in file1: #it assume it is text file (it can not work upon binary file)
            line = line.strip()
            try:
                line = int(line)
                reminder = line % 2 
                line = str(line)
                if reminder == 1: #odd number
                    odd.write(line)
                    odd.write("\n")
                else: #even number
                    even.write(line)
                    even.write("\n")
            except ValueError as error:
                print(f"we got invalid value {line} therefore it is skipped")
        odd.close()
        even.close()
except FileNotFoundError as error:
    print(f"{filename} file not found ")
except PermissionError as error:
    print(f"{filename} is directory/folder. it is not file")
except UnicodeDecodeError as error:
    print(f"{filename} is not text file.")
else:
    print('done. numbers copied successfully into files')
    
