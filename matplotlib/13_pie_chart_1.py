import matplotlib.pyplot as plt 

car_companies = [
    "Maruti Suzuki",
    "Mahindra",
    "Tata Motors",
    "Hyundai",
    "Toyota",
    "Kia",
    "Skoda Volkswagen",
    "JSW MG Motor",
    "Honda",
    "Renault"
]

# List 2: Annual sales figures (units) for calendar year 2025
sales_2025 = [

    1786226,  # Maruti Suzuki
    592771,   # Mahindra
    567607,   # Tata Motors
    559558,   # Hyundai
    320703,   # Toyota
    259043,   # Kia
    108277,   # Skoda Volkswagen
    65614,    # JSW MG Motor
    62576,    # Honda
    36420     # Renault
]

# List 3: Hex color codes representing each company's branding
company_colors = [
    "#eeeeee",  # Maruti Suzuki (Nexa/Corporate Blue)
    "#DD1D25",  # Mahindra (Twin Peaks Red)
    "#005A9C",  # Tata Motors (Dark Blue/Teal theme)
    "#bbbbbb",  # Hyundai (Deep Navy Blue)
    "#EB0A1E",  # Toyota (Racing Red)
    "#05141F",  # Kia (Midnight Black/Dark Navy)
    "#009FDF",  # Skoda Volkswagen (Electric Cyan/Blue)
    "#9E1F15",  # JSW MG Motor (Metallic Red)
    "#0072C6",  # Honda (Classic Blue)
    "#FFCC00"   # Renault (Diamond Yellow)
]
plt.pie(sales_2025,labels=car_companies,colors=company_colors,autopct='%0.1f%%')
plt.title("Car company share 2025")
plt.legend(loc='lower left')
plt.show()

