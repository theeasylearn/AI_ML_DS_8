#list 
teacher = {"name":"Ankit","age":40,"email":"ankit@gmail.com","weight":75.25,"gender":True,"secret":None}
print(teacher)
print(teacher['name'])
#we can update value as well 
teacher['age'] = 41
print(teacher['age'])
#we can delete key value pair
del teacher['secret']
#we can add new key value pair 
teacher['city'] = 'bhavnagar'
print(teacher)