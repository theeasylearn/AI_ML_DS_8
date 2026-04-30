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
                print("let us insert new tour")
            elif tour_choice == 2:
                print("let us display tours")
            elif tour_choice == 3:
                print("lt us update tour")
            elif tour_choice == 4:
                print("let us delete tour")
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
                print("let us insert new transaction")
            elif transaction_choice==2:
                print("let us display all transaction of particular tour")
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