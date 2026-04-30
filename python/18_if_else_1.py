#write a program to findout square or qube of given number. if number is odd calculate & display square if number is even calculate and display cube.
number = int(input("Enter any number")) # 10
reminder = number % 2 
if reminder==0: #== != < > <= >=
    result = number * number * number # 10 * 10 * 10 = 1000
    print(f" qube is {result}") 
else:
    result = number * number # 10 * 10 = 100 
    print(f" square is {result}") 

print("Good bye.")
