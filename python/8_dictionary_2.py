course = {'name':'English','duration':90,'fees':9999.33,'certified':True,'exam':None}
print(course)
print(course['name']) #english
print(course.get('duration')) #90
print(course.get('teacher')) #error
print(course.keys()) #name duration fees certified exam
print(course.values()) # English 90 9999.33 True None
#copy dictionary 
#bad way 
# course2 = course #create reference (mirror copy)
#right way 
course2 = course.copy()
course2.clear()
print("course 2",course2)
print("course",course)
print("items in course",course.items())

book = ['name','author','price','pages','isbnno']
print(book)
#now i want to create dictionary using list 
book1 = dict.fromkeys(book)
print(book1)
book1['name'] = 'Mastering Python'
book1['price'] = 1000
book1.update({'pages':300})
book1.update({'publisher':'the easylearn'})
print(book1)
book1.pop('isbnno')
print(book1)
book1.popitem() #last key value pair
print(book1)
