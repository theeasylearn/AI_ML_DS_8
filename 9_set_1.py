fruits = {'apple','banana','mango','pinapple','apple'}
print(fruits)
#create list which has some duplicate numbers
numbers = [12, 18, 25, 31, 37, 42, 48, 53, 57, 61, 42, 70, 74, 78, 82, 86, 31, 92, 96, 99]
print(numbers)
#remove all duplicate values from list
unique_numbers = set(numbers)
print(unique_numbers)
#add some value into fruits 
fruits.add('kiwi')
fruits.add('cherry')
fruits.add('banana') #duplicate value will be ignored.
print(fruits)
#remove value from set 
fruits.remove('kiwi')
# fruits.remove('coconut') #return keyerror in case of item not found
print(fruits)

