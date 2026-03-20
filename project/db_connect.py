import mysql.connector as con
import mysql.connector.errors as con_error

try: 
    database = con.connect(host='localhost',user='root',passwd='',database='ai_ml_ds_8',port='3306')
    print("Database connection created....")
    my_cursor = database.cursor(dictionary=True)
except con.Error as err:
    print("oops there is problem in connection read detail below")
    print(err.errno)
    print(err.msg)

#create function (insert, update, delete )
def RunQuery(sql,values,message):
    try:
        my_cursor.execute(sql,values)
        #save changes into database 
        database.commit()
        if my_cursor._rowcount == 1:
            print(message)
    except con_error.Error as e:
        print("oops something went wrong, you got an error. read detail below  & contact developer")
        print(e.errno)
        print(e.msg)
def FetchTable(sql,values=None):
    try:
        if values == None:
            my_cursor.execute(sql) 
        else:
            my_cursor.execute(sql,values)
        table = my_cursor.fetchall()
        return table 
    except con_error.Error as e:
        print("oops something went wrong, you got an error. read detail below  & contact developer")
        print(e.errno)
        print(e.msg)
        return None
    