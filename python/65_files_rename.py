import os 
#example of rename file 
try:
    old_file_name = input("Enter existing file name to rename it")
    new_file_name = input("Enter new file name")
    os.rename(old_file_name,new_file_name)
    print('file renamed successfully.')
except FileNotFoundError as error:
    print(f"{old_file_name} not found")
except FileExistsError as error:
    print(f"{new_file_name} already exists")