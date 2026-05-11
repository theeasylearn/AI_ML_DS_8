import pandas as pd 
ipl_titles = {
    # Teams with titles
    "Mumbai Indians": 5,
    "Chennai Super Kings": 5,
    "Kolkata Knight Riders": 3,
    "Royal Challengers Bengaluru": 1,  # Won in 2025
    "Rajasthan Royals": 1,
    "Sunrisers Hyderabad": 1,
    "Gujarat Titans": 1,
    
    # Teams with no titles
    "Delhi Capitals": 0.0,
    "Punjab Kings": 0,
    "Lucknow Super Giants": 0
}
#create Series from dictionary
s1 = pd.Series(ipl_titles,name='IPL Trophy')
print(s1)