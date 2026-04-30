# write a program to calculate amount of profit or loss or break even using given purchase & sale_price = int(input("Enter sell price")) price
#input purchase price, sale price 
purchase_price = int(input("Enter purchase price")) # 100
sale_price = int(input("Enter sell price")) # 120

#calculate difference (process/expression)
difference = sale_price - purchase_price #20

if difference>0: # == != < > <= >=
    print(f"profit amount is {difference}")

elif difference<0: # == != < > <= >=
    print(f"loss amount is {difference}")

else:
    print("No profit No loss")

print("Good bye")