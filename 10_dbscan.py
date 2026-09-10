import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
# ============================================
# 1. Download Chicago crime data
# ============================================
url = (
    "https://data.cityofchicago.org/resource/"
    "ijzp-q8t2.csv"
    "?$limit=5000"
)

#load data 
df = pd.read_csv(url)
# print(df)

#create input features 
x = df[
    [
        "latitude",
        "longitude",
    ]
]

#drop na 
x = x.dropna()
# print(x)

#create model 
model = DBSCAN(eps=0.005,min_samples=10)

labels = model.fit_predict(x)

print(labels)
#add lables into dataset
x['clusters'] = labels
print(x.head(100))

#print clusterwise count 
print(x["clusters"].value_counts())

#create chart
plt.figure(figsize=(10,10))

plt.scatter(x['latitude'],x['longitude'],s=10,c=x['clusters'])
plt.xlabel("Latitude")
plt.ylabel("Longitude")
plt.show()