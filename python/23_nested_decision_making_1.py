''' 
    write a program to calculate & display gross annual income, tax and net income from  given monthly income as per below income tax rule 

    annual income                           Tax Rate
    Above Rs. 24,00,000                     30%
    From Rs. 20,00,001 to Rs. 24,00,000	    25%
    From Rs. 16,00,001 to Rs. 20,00,000	    20%
    From Rs. 12,00,000 to Rs. 16,00,000	    15%
    below 12,00,000                          0%

    steps 
    1) accept monthly income 
    2) calculate annual income 
    3) calculate tax as per rule
    4) calculate net income using gross annual income and tax 
    5) display gross income, tax, net income
'''    
# step 1
monthly_income = float(input("enter monthly income"))
if monthly_income<0:
    print("invalid monthly income")
else:
    # step 2
    annual_income = monthly_income * 12 
    tax  = None
    # step 3
    if annual_income<1200000:
        tax = 0
    elif annual_income>=1200000 and annual_income<1600000:
        tax = (annual_income * 15) / 100
    elif annual_income>=1600001 and annual_income<2000000:
        tax = (annual_income * 20) / 100
    elif annual_income>=2000001 and annual_income<2400000:
        tax = (annual_income * 25) / 100
    else:
        tax = annual_income * 0.30
    # step 4
    net_income = annual_income - tax 
    #step 5
    print("Gross income =",annual_income," Tax = ",tax," Net income = ",net_income)