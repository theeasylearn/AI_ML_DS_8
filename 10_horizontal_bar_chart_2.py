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
bar_colors = [
    "#004BA0", # Mumbai Indians (Blue)
    "#FFFF00", # Chennai Super Kings (Yellow)
    "#3A225D", # Kolkata Knight Riders (Purple)
    "#EA1B85", # Rajasthan Royals (Pink)
    "#FF822A", # Sunrisers Hyderabad (Orange)
    "#1B2133", # Gujarat Titans (Navy Blue)
    "#EC1C24", # Royal Challengers Bengaluru (Red)
    "#00B7F1"  # Deccan Chargers (Sky Blue)
]
plt.figure(figsize=(12,10)) #1st value is for width and 2nd for height
#create horizontal chart
plt.barh(ipl_teams,title_wins,color=bar_colors,edgecolor='black')
plt.xlabel('title win')
plt.ylabel('IPL team name')
plt.title("IPL Trophy Wins data")
plt.savefig('ipl.jpeg') #this method must be called before show method.
plt.show()