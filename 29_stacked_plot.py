import matplotlib.pyplot as plt 
leh_march_2026 = [
    -5.0, -5.0, -1.0, 2.0, 4.0, 5.0, 3.0, 1.0, 3.0, 2.0,
    2.0, -2.0, -4.0, -3.0, -2.0, -5.0, -5.0, -2.0, -1.0, -2.0,
    -4.0, -4.0, -3.0, -5.0, -3.0, -1.0, -1.0, 0.0, 2.0, 3.0, 1.0
]

# Dras day-wise daily mean temperature in Celsius 
# (Reflecting the midpoints of its typical deep freeze to sunny fluctuations)
dras_march_2026 = [
    -8.5, -8.0, -7.5, -6.0, -4.5, -4.0, -4.0, -5.0, -6.5, -5.0,
    -3.5, -3.0, -2.5, -3.0, -7.0, -5.0, -5.5, -8.0, -8.5, -6.0,
    -4.5, -3.5, -4.0, -3.5, -3.5, -2.0, -2.5, -3.5, -4.0, -3.0, -4.5
]
dates = range(1,32)

plt.stackplot(dates,leh_march_2026,dras_march_2026,colors=['yellow','orange'],labels=['Leh','Dras'])
plt.xlabel('dates')
plt.ylabel('temperature ')
plt.title('march 26 temperature leh vs dras')
plt.legend()
plt.grid(which='major')
plt.show()

