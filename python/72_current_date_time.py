from datetime import datetime as dt 

#create object to store current date 

now = dt.now()
week = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
# print(now.weekday)
# print(now.day)
# print(now.month)
# print(now.year)
# print(now.hour)
# print(now.minute)
# print(now.second)
today = week[now.weekday()] + " " + str(now.day) + "/" + str(now.month) + "/" + str(now.year)
print(today)

time = str(now.hour) + ":" + str(now.minute)
print("current time ",time)

