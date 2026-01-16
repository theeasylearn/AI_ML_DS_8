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
'''    
# step 1
monthly_income = float(input("enter monthly income"))
# step 2
annual_income = monthly_income * 12 
# step 3

# step 4
