import os 
filename = input("Enter file name to delete ")
try:
    os.remove(filename)
except FileNotFoundError as error:
    print(f"{filename} not found")
except PermissionError as e:
    print(f"{filename} is directory/folder")
    print("args:", e.args)
    print("type:", e.__class__)
    print("message:", str(e))
    print("traceback:", e.__traceback__)
else:
    print(f"{filename} has been deleted successfully")
finally:
    print("good bye...")
