#insert new record into tour table
#import db_connect 
import db_connect as db
#create cursor object
my_cursor = db.database.cursor()

#build insert statement 
sql = "insert into tour (title,detail,start_date,total_days) values(%s,%s,%s,%s)"

#create list that has 4 values as there are 4 placeholder (%s) in above sql statement 
values = ['water park trip','shankus water park 1 day picnic','2026-03-31',1]

#execute sql statement 
my_cursor.execute(sql,values)

#save changes into database 
db.database.commit()

#display how many rows has been effected by sql statement
print(my_cursor._rowcount)