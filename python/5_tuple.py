#concept of tuples 
places = ("bhavnagar","baroda","rajkot","ahmedabad","surat") #size = 5
#           0           1           2       3           4
#always use () to create tuple
box = (100,True,'Car',3.1415)
print(places)
#display 0th place
print(places[0]) #bhavnagar
#display 1st, 2nd and 3rd places 
print(places[1:4])
#display all places from 2nd position onwards
print(places[2:])
# places[0] = 'abc' #error because tuple is read only (immutable)
print(box)

print('good bye')