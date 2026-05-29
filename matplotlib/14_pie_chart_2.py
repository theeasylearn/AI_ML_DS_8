import matplotlib.pyplot as plt

car_companies = ["Maruti Suzuki", "Mahindra", "Tata Motors", "Hyundai", "Toyota", "Kia", "Skoda Volkswagen", "JSW MG Motor", "Honda", "Renault"]
sales_2025 = [1786226, 592771, 567607, 559558, 320703, 259043, 108277, 65614, 62576, 36420]
company_colors = ["#002C6C", "#DD1D25", "#005A9C", "#002C5F", "#EB0A1E", "#05141F", "#009FDF", "#9E1F15", "#0072C6", "#FFCC00"]

# 1. Create a wider figure to give the legend its own space
plt.figure(figsize=(12, 6))

# 2. Plot the pie WITHOUT text labels on the slices (use only percentages)
wedges, texts, autotexts = plt.pie(
    sales_2025, 
    colors=company_colors, 
    autopct='%1.1f%%', 
    startangle=140,
    pctdistance=0.8
)

# 3. Position legend outside right. 
# (1.05, 0.5) moves it 5% past the right edge of the chart, centered vertically.
plt.legend(
    wedges, 
    car_companies,
    title="Car Companies",
    loc="center left",
    bbox_to_anchor=(1.05, 0.5),
    fontsize=10
)

plt.title("Indian PV Market Share 2025", fontsize=14, fontweight='bold', pad=20)

# 4. CRITICAL: Use bbox_inches='tight' if saving, or tight_layout() so the legend isn't clipped
plt.tight_layout()
plt.show()