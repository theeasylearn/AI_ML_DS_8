'''
### Movie Recommendation Using Apriori

In this example, the Apriori algorithm is used to discover relationships between movies based on users' movie preferences. A real-world MovieLens dataset is used, where each user has rated multiple movies.

For association rule mining, movies with a sufficiently high rating are considered movies that the user **liked**. Each user's collection of liked movies is treated as a single transaction. Apriori then identifies frequently occurring combinations of movies and generates association rules based on their support, confidence, and lift.

For example, if many users who liked **Movie A** also liked **Movie B**, Apriori may generate the rule:

**Movie A → Movie B**

This rule can then be used to recommend **Movie B** to users who have shown interest in **Movie A**.

The objective of this example is to demonstrate how **Association Rule Learning can be applied to a real-world movie recommendation problem**.

dataset download link - https://grouplens.org/datasets/movielens/100k/
'''
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# Load ratings
ratings = pd.read_csv(
    "ml-100k/u.data",
    sep="\t",
    names=["UserID", "MovieID", "Rating", "Timestamp"]
)

movies = pd.read_csv(
    "ml-100k/u.item",
    sep="|",
    encoding="latin-1",
    header=None,
    usecols=[0, 1],
    names=["MovieID", "MovieTitle"]
)
# Keep movies that users liked
liked = ratings[ratings["Rating"] >= 4]

# Add movie names
liked = liked.merge(
    movies,
    on="MovieID"
)

# Create one transaction for each user
transactions = (
    liked.groupby("UserID")["MovieTitle"]
    .apply(list)
    .tolist()
)


# Convert transactions to binary format
encoder = TransactionEncoder()
data = encoder.fit_transform(transactions)

df = pd.DataFrame(
    data,
    columns=encoder.columns_
)

print("NUMBER OF USERS:", len(transactions))
print("NUMBER OF MOVIES:", len(df.columns))
exit(0)
# Find frequent movie combinations
frequent_itemsets = apriori(
    df,
    min_support=0.05,
    use_colnames=True
)

print("\nFREQUENT MOVIE ITEMSETS")
print(frequent_itemsets)

# Generate association rules
rules = association_rules(
    frequent_itemsets,
    metric="confidence",
    min_threshold=0.30
)

# Keep useful columns
rules = rules[
    [
        "antecedents",
        "consequents",
        "support",
        "confidence",
        "lift"
    ]
]

# Keep positive associations
rules = rules[
    rules["lift"] > 1
]

# Sort by lift
rules = rules.sort_values(
    "lift",
    ascending=False
)

print("\nMOVIE ASSOCIATION RULES")

for _, rule in rules.head(20).iterrows():

    antecedent = ", ".join(rule["antecedents"])
    consequent = ", ".join(rule["consequents"])

    print(f"{antecedent} -> {consequent}")
    print(f"Support: {rule['support']:.2%}")
    print(f"Confidence: {rule['confidence']:.2%}")
    print(f"Lift: {rule['lift']:.2f}")
    print("-" * 50)