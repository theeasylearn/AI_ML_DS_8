#insert new record into tour table
#import db_connect 
import python.project.db_connect as db
#create cursor object
my_cursor = db.database.cursor()

#build insert statement 
sql = "insert into tour (title,detail,start_date,total_days) values(%s,%s,%s,%s)"

#accept input from user 
title = input("Enter tour title")
detail = input("Enter tour detail")
start_date = input("Enter start date of tour")
total_days = int(input("Enter no of days for tour"))

#create list that has 4 values as there are 4 placeholder (%s) in above sql statement 
values = [title,detail,start_date,total_days]

#execute sql statement 
my_cursor.execute(sql,values)

#save changes into database 
db.database.commit()

#display how many rows has been effected by sql statement
# print(my_cursor._rowcount)
if my_cursor._rowcount == 1:
    print("tour has been added ")