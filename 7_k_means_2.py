import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# STEP 1: Create dataset
data = {
    "Area": [
        "A", "B", "C", "D",
        "E", "F", "G", "H",
        "I", "J", "K", "L"
    ],

    "Direction": [
        "North", "North", "North", "North",
        "East", "East", "East", "East",
        "South", "South", "South", "South"
    ],

    "Distance": [
        2, 3, 4, 5,
        10, 11, 12, 13,
        20, 21, 22, 23
    ],

    "DailyOrders": [
        95, 90, 100, 85,
        55, 60, 50, 58,
        20, 25, 18, 22
    ]
}

#step 2 create dataframe
df = pd.DataFrame(data)

#step 3 select input data features (notice direction is skipped)

x = df [ [
    "Distance",
    "DailyOrders"
]]

#step 4 scale data 
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

#step 5 find k 
inertia = [] #empty list 
for k in range(1,7):
    model = KMeans(n_clusters=k,random_state=42,n_init=1)
    model.fit(x_scaled)
    inertia.append(model.inertia_)

#create chart 
plt.figure(figsize=(8,6))
plt.plot(range(1,7),inertia,marker='o')
plt.xlabel("Number of clusters")
plt.ylabel("Inertia")
plt.show()

#create actual model 
model = KMeans(n_clusters=3,random_state=42,n_init=1)
model.fit(x_scaled)
print(model.labels_) 
#insert labels into dataframe
df['Clusters'] = model.labels_
print(df)
