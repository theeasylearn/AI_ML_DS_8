# List of fruits
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes", "Pineapple", "Strawberry", "Papaya", "Watermelon", "Cherry"]

# Tuple of 10 countries
countries = ("India", "USA", "China", "Brazil", "Australia", "Japan", "Germany", "France", "UK", "Canada")

# String of vegetables (comma-separated)
veggies = "Carrot Broccoli Spinach Tomato Onion Potato Bell Pepper Cucumber Eggplant Cabbage"

# Dictionary of Virat Kohli details
kohli = {
    "name": "Virat Kohli",
    "born": "November 5, 1988",
    "age": 37,  # As of 2026
    "team": "India",
    "role": "Batsman",
    "batting_style": "Right-hand bat",
    "bowling_style": "Right-arm medium",
    "odi_matches": 308,
    "odi_runs": 14557
}

# Print all to verify
print("Fruits:", fruits)
print("Countries:", countries)
print("Veggies:", veggies)
print("Kohli:", kohli)

favorite_fruit = input("What is your favourite fruit?")
isFound = favorite_fruit in fruits
print(isFound) 

isNotFound = favorite_fruit not in fruits
print(isNotFound)

your_country = input("Where are you from?")
isFound = your_country in countries
print(isFound) 


key = input("what do you want to know about virat kohli?")
isFound = key in kohli
print(isFound) 

favourite_vegi = input("What is your favourite vegis")
isFound = favourite_vegi in veggies
print(isFound) 
