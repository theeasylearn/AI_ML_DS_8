import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# Transactions
transactions = [
    ["Bread", "Milk"],
    ["Bread", "Milk"],
    ["Bread", "Milk"],
    ["Bread", "Milk"],
    ["Bread", "Milk"],
    ["Bread", "Milk"],
    ["Bread", "Butter"],
    ["Bread", "Butter"],
    ["Milk"],
    ["Milk"],
    ["Butter"],
    ["Butter"],
    ["Butter"],
    ["Butter"],
    ["Butter"]
]

# Convert transactions to 0/1 format
encoder = TransactionEncoder()
# Convert transactions into Boolean data
data = encoder.fit_transform(transactions)

df = pd.DataFrame(data, columns=encoder.columns_)

print("TRANSACTION DATA")
print(df)

# Find frequent itemsets
frequent_itemsets = apriori(df,min_support=0.40,use_colnames=True)
print("\nFREQUENT ITEMSETS")
print(frequent_itemsets)

# Generate association rules
rules = association_rules(
    frequent_itemsets,
    metric="confidence", # metric="confidence" means If someone buys the items on the left, how often do they also buy the items on the right?
    min_threshold=0.50 #Only generate rules having at least 50% confidence.
)

# print("\nASSOCIATION RULES")
for index, rule in rules.iterrows():
    print(f"{rule['antecedents']} -> "f"{rule['consequents']}")
    print(f"Support: {rule['support']:.2%}")
    print(f"Confidence: {rule['confidence']:.2%}")
    print(f"Lift: {rule['lift']:.2f}")
    print("-" * 40)

# Find strong rules
strong_rules = rules[(rules["confidence"] >= 0.60) &(rules["lift"] > 1)]

print("\nSTRONG RULES")

for index,rule in strong_rules.iterrows():
    print(f"{rule['antecedents']} -> "f"{rule['consequents']}")
    print(f"Support: {rule['support']:.2%}")
    print(f"Confidence: {rule['confidence']:.2%}")
    print(f"Lift: {rule['lift']:.2f}")
    print("-" * 40)