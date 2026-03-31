#write a program to write data into file 
filename = "example.txt"
mode = "w"
# if file already exists, python will replace content of the file with new content
with open(filename,mode) as file:
    content = input("Write some text and press enter key ")
    file.write(content) #write user given content into file
    print("data saved successfully....")

print("good bye")
