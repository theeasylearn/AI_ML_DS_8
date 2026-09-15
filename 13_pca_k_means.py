# Step 1: Import libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# Step 2: load dataset
#create dataframe 
X = pd.read_csv("patient_health_data.csv")
patient = X[['Patient']]
#select input features 
X = X[
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

#create pca object
pca = PCA(n_components=2)
pca_df = pca.fit_transform(x_scaled)
del x_scaled 

#convert it into dataframe 
pca_df = pd.DataFrame(pca_df,columns=['PC-1','PC-2'])

print("PC-1 variance ",pca.explained_variance_ratio_[0])
print("PC-2 variance ",pca.explained_variance_ratio_[1])

# pca_df["Patient"] = df["Patient"]
# print(pca_df)


#step 5 find k 
inertia = [] #empty list 
for k in range(1,7):
    model = KMeans(n_clusters=k,random_state=42,n_init=1)
    model.fit(pca_df)
    inertia.append(model.inertia_)

#create chart 
plt.figure(figsize=(8,6))
plt.plot(range(1,7),inertia,marker='o')
plt.xlabel("Number of clusters")
plt.ylabel("Inertia")
plt.show()

#create actual model 
model = KMeans(n_clusters=3,random_state=42,n_init=1)
model.fit(pca_df)
print(model.labels_) 
#insert labels into dataframe
X['Clusters'] = model.labels_
X['Patient'] = patient['Patient']
print(X)