# write a program to calculate and display batter strike 
while 1!=2:
    try:
        runs = int(input("Enter batter's run"))
        balls = int(input("Enter balls played by batter"))
        strike_rate = runs / balls * 100
        print(f"batter's strike rate = {strike_rate}")
        break #break the loop 
    except ValueError:
        print("invalid input, only numbers are allowed")
    except ZeroDivisionError:
        print("ball can not be zero")
    