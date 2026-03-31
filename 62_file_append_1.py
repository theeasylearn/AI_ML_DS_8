#write a program to write data into file 
filename = input("enter file name to write data into file")
mode = "a"
# in append mode, if file already exists, python will append  content at the end file 
with open(filename,mode) as file:
    content = input("Write some text and press enter key ")
    file.write("\n" + content) #write user given content into file
    print("file updated successfully....")

print("good bye")
