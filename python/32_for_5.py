#write a program to count vowels in given string using for loop
line = input("What is your name?")
vowels = ['a','e','i','o','u']
count = 0
for letter in line:
    if str.lower(letter) in vowels:
        count = count + 1
print(count)