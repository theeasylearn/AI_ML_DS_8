# task is to implement try except else finally block in this example
import os 
directory_name = input("enter directory name to create it")
os.mkdir(directory_name)
key = input("Directory created.... press enter to continue")
print(os.getcwd())
os.chdir(directory_name)
key = input("Directory changed .... press enter to continue")
print("now present working directory is ",os.getcwd())
directory_name = input("enter another directory name to create it")
os.mkdir(directory_name)
key = input("Another directory created.... press enter to continue")
os.rmdir(directory_name)
print("Directory has been deleted")
