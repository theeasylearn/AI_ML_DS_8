def getMerit(maths,science,english,computer,drawing,history):
    total = maths + science + english 
    return total 

m = int(input("Mathematics : "))
s = int(input("Science     : "))
e = int(input("English     : "))
c = int(input("Computer    : "))
d = int(input("Drawing     : "))
h = int(input("History     : "))

# wrong way of calling function as it generate logical error
# total = getMerit(c,d,h,m,s,e)
# perfect way of calling function that avoid logical error
total = getMerit(computer=c,drawing=d,history=h,english=e,maths=m,science=s)
print(total)

