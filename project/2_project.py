import db_connect as db
import mysql.connector.errors as con_error
my_cursor = db.database.cursor(dictionary=True)
def DisplayTour():
    sql = "select id,title,detail,date_format(start_date,'%d-%m-%Y') as start_date,total_days from tour order by id "
    table = db.FetchTable(sql)
    if table != None:
        #fetch one row 
        # first_row = my_cursor.fetchone()
        # print(first_row) #will display 1st row as dictionary
        # print(table)
        #fetch all rows one by one and display it 
        print(f"{'id':<6} {'title':<32} {'detail':<40}  {'total_days':<8} {'start_date'}")
        print("_"*100)
        for row in table:
            output = f"{row['id']:<6} {row['title']:<32} {row['detail']:<40}  {row['total_days']:<8} {row['start_date']}"
            print(output)
while True:
    print("Press 1 for tour management")
    print("Press 2 for transaction management")
    print("Press 0 to exit from program")
    choice = int(input("Enter hour choice"))
    if choice == 1:
        while True:
            print("tour management")
            print("_"*100)
            print("press 1 to add new tour")
            print("Press 2 to display all tours")
            print("Press 3 to update tour")
            print("Press 4 to delete tour")
            print("press 0 to exit from tour management")
            tour_choice = int(input("Enter your choice"))
            if tour_choice == 1:
                sql = "insert into tour (title,detail,start_date,total_days) values(%s,%s,%s,%s)"
                #accept input from user 
                title = input("Enter tour title")
                detail = input("Enter tour detail")
                start_date = input("Enter start date of tour")
                total_days = int(input("Enter no of days for tour"))

                #create list that has 4 values as there are 4 placeholder (%s) in above sql statement 
                values = [title,detail,start_date,total_days]
                db.RunQuery(sql,values,"tour has been added ")
            elif tour_choice == 2:
                DisplayTour()
            elif tour_choice == 3:
                sql = "update tour set title=%s,detail=%s,start_date=%s,total_days=%s where id=%s"
                title = input("Enter tour title")
                detail = input("Enter tour detail")
                start_date = input("Enter tour start date")
                total_days = int(input("Enter tour no days"))
                id = int(input("Enter tour id "))
                #create list of size 6 as there are 6 placeholder in sql statement 
                values = [title,detail,start_date,total_days,id]
                #execute sql statement
                db.RunQuery(sql,values,"trip updated successfully")
            elif tour_choice == 4:
                #build query(sql statement)
                sql = "delete from tour where id=%s"
                id = int(input("enter tour id to delete tour"))
                #create list of size 1
                values = [id]
                db.RunQuery(sql,values,"trip has been removed successfully")
            elif tour_choice == 0:
                print("exit from tour management")  
                break #inner loop 
            else:
                print("invalid choice")

    elif choice == 2:
        print("let us do transaction management")
        while True:
            print("Press 1 to insert new transaction")
            print("press 2 to display all transaction (particular tour)")
            print("press 3 to update transaction")
            print("press 4 to delete transaction")
            print("press 0 to exit to main menu")
            transaction_choice = int(input("Enter your choice"))
            if transaction_choice==1:
                DisplayTour()
                
                tourid = int(input("Enter tour id"))
                amount = int(input("Enter transaction amount"))
                print("Press 1 for income")
                print("Press 2 for expense")
                transaction_type = int(input("Enter your transaction type (1 or 2)"))
                description = input("Enter transaction description")
                challan_number = input("Enter challan number")
                sql = "insert into transaction (tourid,amount,transaction_type_flag,description,challan_number) values (%s,%s,%s,%s,%s)" # %s placeholder
                values = [tourid,amount,transaction_type,description,challan_number]
                db.RunQuery(sql,values,"Transaction added successfully")
            elif transaction_choice==2:
                DisplayTour()
                tourid = int(input("Enter tour id"))
                sql = "select * from transaction where tourid=%s"
                values = [tourid]
                table = db.FetchTable(sql,values)
                if table != None:
                    print(table) #2d list (list of dictionary)
                    for row in table:
                        
            elif transaction_choice==3:
                print("let us update transaction")
            elif transaction_choice==4:
                print("let us delete transaction")
            elif transaction_choice==0:
                print("exit to main menu")
                break #inner loop break
            else:
                print("invalid choice")
            
    elif choice == 0:
        break #loop stop 
    else:
        print("invalid choice")