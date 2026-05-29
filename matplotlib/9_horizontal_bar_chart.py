import matplotlib.pyplot as plt
ipl_teams = [
    "Mumbai Indians", 
    "Chennai Super Kings", 
    "Kolkata Knight Riders", 
    "Rajasthan Royals", 
    "Sunrisers Hyderabad", 
    "Gujarat Titans", 
    "Royal Challengers Bengaluru", 
    "Deccan Chargers"
]
# Corresponding title wins for each team
title_wins = [5, 5, 3, 1, 1, 1, 1, 1]

#create horizontal chart
plt.barh(ipl_teams,title_wins,color='yellow',edgecolor='black')
plt.xlabel('title win')
plt.ylabel('IPL team name')
plt.title("IPL Trophy Wins data")
plt.show()