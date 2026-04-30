#update tour 
import python.project.db_connect as db 

#create cursor 
my_cursor = db.database.cursor()

#create sql statement
sql = "update tour set title=%s,detail=%s,start_date=%s,total_days=%s where id=%s"

title = input("Enter tour title")
detail = input("Enter tour detail")
start_date = input("Enter tour start date")
total_days = int(input("Enter tour no days"))
id = int(input("Enter tour id "))

#create list of size 6 as there are 6 placeholder in sql statement 
values = [title,detail,start_date,total_days,id]

#execute sql statement
my_cursor.execute(sql,values)

#save changes
db.database.commit()

#print how many rows updated
print(my_cursor.rowcount, " trip updated")