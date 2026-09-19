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
#encoding
encoder = TransactionEncoder()
data = encoder.fit_transform(transactions)

#create dataframe
df = pd.DataFrame(data,columns=encoder.columns_)
print(df.head(5))

frequent_itemsets = apriori(df,min_support=0.05,use_colnames=True)
# print(frequent_itemsets.head(5))

rules = association_rules(frequent_itemsets,metric='confidence', min_threshold=0.05)

#filter data
rules = rules [rules['lift']>1]
print(rules.head(5))


