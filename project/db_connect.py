import mysql.connector as con
try: 
    database = con.connect(host='localhost',user='root',passwd='',database='ai_ml_ds_8',port='3306')
    print("Database connection created....")
except con.Error as err:
    print("oops there is problem in connection read detail below")
    print(err.errno)
    print(err.msg)