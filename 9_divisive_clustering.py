# ============================================================
# DIVISIVE HIERARCHICAL CLUSTERING
# Example: Grouping 12 Countries
# ============================================================

# Step 1: Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


# ============================================================
# Step 2: Create the dataset
# ============================================================

data = {
    "Country": [
        "India",
        "China",
        "USA",
        "Germany",
        "Japan",
        "Brazil",
        "Canada",
        "Nigeria",
        "Switzerland",
        "Bangladesh",
        "Australia",
        "South Africa"
    ],

    # GDP per capita in USD
    "GDP_per_capita": [
        2700,
        13000,
        85000,
        55000,
        34000,
        11000,
        53000,
        1100,
        100000,
        2700,
        65000,
        6500
    ],

    # Life expectancy in years
    "Life_expectancy": [
        67,
        78,
        77,
        81,
        84,
        76,
        82,
        54,
        84,
        73,
        83,
        62
    ],

    # Internet users as percentage of population
    "Internet_usage": [
        55,
        76,
        97,
        92,
        87,
        81,
        94,
        36,
        96,
        45,
        97,
        75
    ]
}

# Convert dictionary into DataFrame
df = pd.DataFrame(data)

print("Original Dataset:")
# print(df)

#select input features 
X = df[[
    "GDP_per_capita",
    "Life_expectancy",
    "Internet_usage",
]]


#apply scaler 
scaler = StandardScaler()

x_scaled = scaler.fit_transform(X)
# print(x_scaled)

def divisive_clustering(X, countries, number_of_clusters=4):
    #create dictionary which has all the clusters 
    clusters = {
        0: list(range(len(countries))),
    }
    next_cluster_id = 1
    #run loop to crate 4 clusters 
    while len(clusters)<number_of_clusters:
        # findout upon which key we should work to create new clusters 
        largest_cluster_id = max(clusters,key=lambda cluster_id : len(clusters[cluster_id]))
        #extract data 
        indexes = clusters[largest_cluster_id]
        cluster_data = X[indexes]
        #apply kmean algorithm 
        model = KMeans(random_state=42,n_clusters=2,n_init=10)
        model.fit_transform(cluster_data)
        # print(model.labels_)
        cluster_1 = []
        cluster_2 = []
        for label,index in zip(model.labels_,indexes):
            if label == 0:
                cluster_1.append(index)
            else:
                cluster_2.append(index)
        del clusters[largest_cluster_id]
        clusters[next_cluster_id] = cluster_1
        next_cluster_id= next_cluster_id + 1 #2
        clusters[next_cluster_id] = cluster_2
        next_cluster_id= next_cluster_id + 1 #
    return clusters
# print(df["Country"].tolist())
clusters = divisive_clustering(x_scaled,df["Country"].tolist(),4)
#clusters add original dataset 
temp = {}
for cluster in clusters.items():
    current_cluster = cluster[0]
    for index in cluster[1]:
        #update original dataset
        temp[index] = current_cluster
df["cluster"] = temp
print(df)
#task display dataframe as scatter chart
