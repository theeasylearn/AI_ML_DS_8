# asian_countries = ["China", "India", "Japan", "South Korea", "Thailand", "Vietnam", "Indonesia", "Malaysia", "Philippines", "Singapore"]
def printNames(*countries):
    # countries is tuple 
    for item in countries:
        print(item)


#call function
# printNames("China", "India", "Japan")
printNames("China", "India", "Japan", "South Korea", "Thailand", "Vietnam", "Indonesia", "Malaysia", "Philippines", "Singapore")