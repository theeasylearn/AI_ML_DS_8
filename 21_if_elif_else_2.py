# write a program to findout whether given shape is potrait, landscape or square using given length and width if elif decision making statement if 

#input: length & width 

length = int(input("Enter length"))
width = int(input("Enter width"))

if length>width: # == != < > <= >=
    print("given shape is portrait")
elif length<width:
    print("given shape is landscape")
else:
    print("given shape is square")

