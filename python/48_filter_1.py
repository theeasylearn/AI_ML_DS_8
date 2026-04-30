numbers = [12, 45, 78, 23, 56, 91, 34, 67, 88, 19, 72, 54, 39, 84, 26, 95, 41, 60, 73, 29]
print(numbers)
#filter number divisible by 5
filtered_numbers = filter(lambda num: num%5==0,numbers)
print(list(filtered_numbers))