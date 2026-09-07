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
print(df)


# ============================================================
# Step 3: Select the input features
# ============================================================

X = df[
    [
        "GDP_per_capita",
        "Life_expectancy",
        "Internet_usage"
    ]
]


# ============================================================
# Step 4: Standardize the data
# ============================================================

# GDP has values such as 1,100 and 100,000.
# Life expectancy has values around 50-85.
# Internet usage has values around 30-100.
#
# Because their scales are different, we standardize them.

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)


# ============================================================
# Step 5: Create a function for Divisive Clustering
# ============================================================

def divisive_clustering(X, countries, number_of_clusters=4):

    # Initially, all countries belong to one cluster
    clusters = {
        0: list(range(len(countries)))
    }

    next_cluster_id = 1

    # Continue splitting until desired number of clusters
    while len(clusters) < number_of_clusters:

        # ----------------------------------------------------
        # Find the largest cluster
        # ----------------------------------------------------

        largest_cluster_id = max(
            clusters,
            key=lambda cluster_id: len(clusters[cluster_id])
        )

        # Get countries belonging to that cluster
        indexes = clusters[largest_cluster_id]

        # Extract their feature values
        cluster_data = X[indexes]

        # ----------------------------------------------------
        # Split the cluster into 2 groups
        # ----------------------------------------------------

        kmeans = KMeans(
            n_clusters=2,
            random_state=42,
            n_init=10
        )

        labels = kmeans.fit_predict(cluster_data)

        # ----------------------------------------------------
        # Create two new clusters
        # ----------------------------------------------------

        cluster_1 = []
        cluster_2 = []

        for i, label in zip(indexes, labels):

            if label == 0:
                cluster_1.append(i)
            else:
                cluster_2.append(i)

        # Remove the original cluster
        del clusters[largest_cluster_id]

        # Add the two new clusters
        clusters[next_cluster_id] = cluster_1
        next_cluster_id += 1

        clusters[next_cluster_id] = cluster_2
        next_cluster_id += 1

    return clusters


# ============================================================
# Step 6: Perform Divisive Clustering
# ============================================================

clusters = divisive_clustering(
    X_scaled,
    df["Country"].tolist(),
    number_of_clusters=4
)


# ============================================================
# Step 7: Display the final clusters
# ============================================================

print("\nFinal Clusters:")
print("----------------")

for cluster_id, indexes in clusters.items():

    print(f"\nCluster {cluster_id}:")

    for index in indexes:
        print("  ", df.loc[index, "Country"])


# ============================================================
# Step 8: Add cluster number to DataFrame
# ============================================================

df["Cluster"] = 0

for cluster_id, indexes in clusters.items():

    for index in indexes:
        df.loc[index, "Cluster"] = cluster_id


# Display final dataset
print("\nFinal Dataset:")
print(df)


# ============================================================
# Step 9: Visualize the clusters
# ============================================================

plt.figure(figsize=(10, 6))

plt.scatter(
    df["GDP_per_capita"],
    df["Life_expectancy"],
    c=df["Cluster"],
    s=100
)

# Add country names to the graph
for i in range(len(df)):

    plt.annotate(
        df.loc[i, "Country"],
        (
            df.loc[i, "GDP_per_capita"],
            df.loc[i, "Life_expectancy"]
        ),
        xytext=(5, 5),
        textcoords="offset points"
    )

plt.xlabel("GDP per Capita (USD)")
plt.ylabel("Life Expectancy (Years)")
plt.title("Divisive Hierarchical Clustering of Countries")

plt.show()