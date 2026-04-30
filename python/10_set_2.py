set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}

#we want to get unique values from both set 
set3 = set1.union(set2)
print(set3) 

#we want to get common value between 2 sets
set4 = set1.intersection(set2)
print(set4)

#we want to get values that is in set1 but not set2
set5 = set1.difference(set2)
print(set5)