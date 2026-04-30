# example of raising exception  
try:
    runs = int(input("Enter batter's run"))
    balls = int(input("Enter balls played by batter"))
    if balls>120 or balls<0:
        raise TypeError('invalid balls played. balls must be in range of 1 to 120')
    strike_rate = runs / balls * 100
except ValueError:
    print("invalid input, only numbers are allowed")
except ZeroDivisionError:
    print("ball can not be zero")
except TypeError as e:
    print(f"error {e}")
else:
    print(f"batter's strike rate = {strike_rate}")
finally:
    print("Good bye")
