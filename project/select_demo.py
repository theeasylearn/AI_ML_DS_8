import db_connect as db
#create cursor 
my_cursor = db.database.cursor(dictionary=True)

#build sql statement(query)
sql = "select id,title,detail,date_format(start_date,'%d-%m-%Y') as start_date,total_days from tour order by id "

#run sql statement
my_cursor.execute(sql) 

#fetch one row 
# first_row = my_cursor.fetchone()

# print(first_row) #will display 1st row as dictionary

table = my_cursor.fetchall() #return 2d array (list of dictionary)
# print(table)
#fetch all rows one by one and display it 
print(f"{'id':<6} {'title':<32} {'detail':<40}  {'total_days':<8} {'start_date'}")
print("_"*100)
for row in table:
    output = f"{row['id']:<6} {row['title']:<32} {row['detail']:<40}  {row['total_days']:<8} {row['start_date']}"
    print(output)