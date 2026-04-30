nations = ("India", "United States","India", "China", "Russia", "Germany", "France", "Japan", "Brazil", "United Kingdom", "Australia","Russia","India")
print(nations)
#count how many india in nations
print("Count of india ",nations.count("India"))
print("Count of Russia ",nations.count("Russia"))
print("Count of Norway ",nations.count("Norway"))
print("Position of Japan ",nations.index("Japan"))
# print("Position of Norway ",nations.index("Norway")) #error index method returns ValueError if item not found
print("Good bye")