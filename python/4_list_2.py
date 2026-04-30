kit = ['books',200,None,True,False,3.14]
pockets = [] #empty list 
print(kit)
print(pockets)
#we can add new items into list 
pockets.append(100) #it will add new item at the end of list 
pockets.append(200) #it will add new item at the end of list 
pockets.append(500) #it will add new item at the end of list 
print(pockets)
#add item @ begining
pockets.insert(0,50)
pockets.insert(0,10)
#insert new item at position
pockets.insert(1,20)
print(pockets)
pockets.insert(2,25)
print(pockets)
# delete 2nd item (remove by position)
pockets.pop(2)
print(pockets)
#remove by value
pockets.remove(50)
# pockets.remove(150) error because item does not exist
pockets[0] = 11 #it will update value at 0th position
print(pockets)
del pockets #remove entire list 
print("good bye")