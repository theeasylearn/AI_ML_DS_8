#write a program to read file numbers.txt which has numbers. if number is odd, write it into odd.txt file otherwise write it into even.txt file 
#1st read content from file
filename = "numbers.txt"
filename2 = "odd.txt"
filename3 = "even.txt"
mode = 'r'
with open(filename,mode) as file1:
    #open other two files in write mode
    odd = open(filename2,"w")
    even = open(filename3,"w")
    for line in file1:
        line = line.strip()
        line = int(line)
        reminder = line % 2 
        line = str(line)
        if reminder == 1: #odd number
            odd.write(line)
            odd.write("\n")
        else: #even number
            even.write(line)
            even.write("\n")
    
    odd.close()
    even.close()
print('done.')
