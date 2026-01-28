'''
        *
      * * 
    * * * 
  * * * *
* * * * *
'''
count = 1
for row in range(6,1,-1):
    for space in range(1,row):
        print(' ',end=' ')
    for astrik in range(0,count):
        print("*",end=' ')
    count=count+1
    print("")


