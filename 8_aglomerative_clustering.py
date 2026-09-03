import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering

from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import dendrogram


# ============================================
# 1. Create customer dataset
# ============================================

data = {
    "Customer": [
        "C1", "C2", "C3",
        "C4", "C5", "C6",
        "C7", "C8", "C9",
        "C10", "C11", "C12"
    ],

    "income": [
        1500000, 1800000, 2000000,
        4500000, 4800000, 5000000,
        8000000, 8500000, 9000000,
        3000000, 3300000, 13500000
    ],

    "Purchases": [
        300000, 400000, 500000,
        1000000, 1100000, 1200000,
        2000000, 2100000, 2200000,
        700000, 800000, 8000000
    ]
}

#create dataframe 
df = pd.DataFrame(data)
# print(df)

#select input features 
x = df [
    [
        "income",
        "Purchases",
    ]
]
# print(x)

#scaler 
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)
print(x_scaled)

#model train 
matrix = linkage(x_scaled,method='ward')

#create plot
plt.figure(figsize=(10,6))

#create dendrogram 
dendrogram(matrix,labels = df["Customer"].values)

plt.xlabel('customer name')
plt.ylabel("Distance")
plt.show()

agglomerative_model = AgglomerativeClustering(n_clusters=4,linkage='ward')

labels = agglomerative_model.fit_predict(x_scaled)

print(labels)

#add label into original dataset 
df['clusters'] =  labels

print(df)