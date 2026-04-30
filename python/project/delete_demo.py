#delete row from table tour
import python.project.db_connect as db 

#create cursor 
my_cursor = db.database.cursor()

#build query(sql statement)
sql = "delete from tour where id=%s"

id = int(input("enter tour id to delete tour"))
#create list of size 1
values = [id]
#execute sql statement
my_cursor.execute(sql,values)
#commit changes 
db.database.commit()
print("no of rows deleted from table",my_cursor.rowcount)
