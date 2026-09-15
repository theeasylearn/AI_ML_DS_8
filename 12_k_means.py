# Step 1: Import libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
# Step 2: load dataset
#create dataframe 
df = pd.read_csv("patient_health_data.csv")
#select input features 
X = df[
    [
        "Age",
        "Systolic_BP",
        "Diastolic_BP",
        "Cholesterol",
        "Glucose",
        "BMI",
        "Heart_Rate",
        "Activity"
    ]
]
#do scaling 
scaler = StandardScaler()
x_scaled = scaler.fit_transform(X)
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