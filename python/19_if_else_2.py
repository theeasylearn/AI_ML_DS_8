# write a program to findout which is cheaper product for purchase from 2 product's weight and price. 
# also display how much cheaper
# input price and weight of 1st product
# input price and weight of 2nd product
price_1 = int(input("Enter 1st product price"))
weight_1 = int(input("Enter 1st product weight"))

price_2 = int(input("Enter 2nd product price"))
weight_2 = int(input("Enter 2nd product weight"))

#calculate price per gram 
price_per_gram_1 = price_1 / weight_1 #price per gram of 1st product
price_per_gram_2 = price_2 / weight_2 #price per gram of 2nd product

#findout cheaper product
if price_per_gram_1<price_per_gram_2: # == != < > <= >=
    print("1st product is cheaper then second product by ",price_per_gram_2 - price_per_gram_1)
else:
    print("2nd product is cheaper then first product by ",price_per_gram_1 - price_per_gram_2)

print("Good bye.")
