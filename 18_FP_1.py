import pandas as pd
from mlxtend.frequent_patterns import fpgrowth, association_rules
# # ============================================================
# STEP 2: LOAD DATASET
# ============================================================
df = pd.read_csv('fp_train_disease.csv')
print("\nDATASET SHAPE:")
print("before drop",df.shape)
df = df.dropna()
print("after drop",df.shape)
print("\nCOLUMNS:")
# print(df.columns.tolist())
frequent_itemsets = fpgrowth(df,min_support=0.05,use_colnames=True)
print("\nFREQUENT SYMPTOM ITEMSETS")
print("-" * 60)
frequent_itemsets = frequent_itemsets.sort_values("support",ascending=False)
# print(frequent_itemsets.head(50))
rules = association_rules(frequent_itemsets,metric="confidence",min_threshold=0.20)
rules = rules[rules['lift']>=1]
rules = rules.sort_values("lift",ascending=False)
print(rules.columns)
for index,rule in rules.iterrows():
    print(f"{' '.join(rule['antecedents'])} -> {' '.join(rule['consequents'])} {round(rule['support'],2)} {round(rule['confidence'],2)} {round(rule['lift'],2)}")