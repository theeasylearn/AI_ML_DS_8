# ============================================================
# PCA - PATIENT HEALTH ANALYSIS
# ============================================================

# Step 1: Import libraries

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
# ============================================================
# Step 2: load dataset
# ============================================================
#create dataframe 
df = pd.read_csv("patient_health_data.csv")
# print(df)

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
# print(X)
#do scaling 
scaler = StandardScaler()
x_scaled = scaler.fit_transform(X)
# print(x_scaled)

#create pca object
pca = PCA(n_components=2)
pca_df = pca.fit_transform(x_scaled)

#convert it into dataframe 
pca_df = pd.DataFrame(pca_df,columns=['PC-1','PC-2'])

print("PC-1 variance ",pca.explained_variance_ratio_[0])
print("PC-2 variance ",pca.explained_variance_ratio_[1])

pca_df["Patient"] = df["Patient"]
print(pca_df)

#display as scatter plot chart 
plt.figure(figsize=(12,10))

plt.scatter(pca_df["PC-1"],pca_df["PC-2"],s=100)
plt.xlabel("PC-1")
plt.ylabel("PC-2")
plt.title("Principal Component Analysis")
# set labels for each points
for i in range(len(pca_df)):
    plt.annotate(pca_df.loc[i,"Patient"],(
        pca_df.loc[i,"PC-1"],
        pca_df.loc[i,"PC-2"]
    ),xytext=(5,5),textcoords="offset points")

plt.axhline(0)
plt.axvline(0)
plt.show()

