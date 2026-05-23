import matplotlib.pyplot as plt 
android_units = [
    67.0, 220.0, 460.0, 760.0, 1005.0, 1110.0, 1245.0, 1260.0, 
    1195.0, 1180.0, 1148.0, 1215.0, 1132.0, 1113.0, 1146.0, 1159.0
]

# iPhone (iOS) units shipped in millions (2010 to 2025)
ios_units = [
    39.9, 72.3, 125.0, 150.2, 169.2, 231.2, 211.8, 216.7, 
    208.8, 191.0, 206.1, 242.0, 232.2, 231.3, 232.1, 247.0
]

years = range(2010,2026)

plt.figure(figsize=(18,10))
plt.bar(years,android_units,color='blue')
plt.bar(years,ios_units,color='#eeeeee',bottom=android_units)
plt.xlabel('years')
plt.ylabel('sales in milions')
plt.title('andorid vs iphone sales data ')
plt.legend()
plt.grid(which='major')
plt.show()
