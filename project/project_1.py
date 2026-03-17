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
                break 
    elif choice == 2:
        print("let us do transaction management")
    elif choice == 0:
        break #loop stop 
    else:
        print("invalid choice")