import pandas as pd
import kagglehub
from pathlib import Path
from mlxtend.frequent_patterns import fpgrowth, association_rules
# ============================================================
# STEP 1: DOWNLOAD DATASET
# ============================================================
path = kagglehub.dataset_download("hemanthhari/symptoms-and-covid-presence")
csv_files = list(Path(path).rglob("*.csv"))
if not csv_files:
    print("File not found")
else:
    #file found 
    file = csv_files[0] 
    # print("Using file:")
    # print(file)
    # # ============================================================
    # STEP 2: LOAD DATASET
    # ============================================================
    df = pd.read_csv(file)
    print("\nDATASET SHAPE:")
    print(df.shape)
    print("\nCOLUMNS:")
    print(df.columns.tolist())
    # ============================================================
    # STEP 3: CLEAN COLUMN NAMES
    # ============================================================
    df.columns = df.columns.str.strip()
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace(" ","_")
    df.columns = df.columns.str.replace("-","_")

    print("\nCLEANED COLUMNS:")
    # print(df.columns.tolist())
    # # ============================================================
    # # STEP 4: SELECT SYMPTOM COLUMNS
    # # ============================================================
    symptom_columns = [
        "fever",
        "tiredness",
        "dry_cough",
        "difficulty_in_breathing",
        "sore_throat",
        "pains",
        "nasal_congestion",
        "runny_nose",
        "diarrhea"
    ]
    available_columns = [] 
    for column in symptom_columns:
        if column in df.columns:
            available_columns.append(column)    
    print("\nSYMPTOM COLUMNS USED:")
    print(available_columns)
    if len(available_columns) == 0:
        raise ValueError("No symptom columns found.")
    # ============================================================
    # STEP 5: CONVERT SYMPTOMS TO BOOLEAN
    # ============================================================
    symptoms = pd.DataFrame(index=df.index)
    for column in available_columns:
        symptoms[column] = df[column].astype(str).isin(
            ["1", "yes", "true", "positive", "present"]
        )

    # ============================================================
    # STEP 6: RENAME COLUMNS
    # ============================================================
    rename_columns = {
        "fever": "Fever",
        "tiredness": "Tiredness",
        "dry_cough": "Dry Cough",
        "difficulty_in_breathing": "Difficulty Breathing",
        "sore_throat": "Sore Throat",
        "pains": "Pains",
        "nasal_congestion": "Nasal Congestion",
        "runny_nose": "Runny Nose",
        "diarrhea": "Diarrhea"
    }
    symptoms = symptoms.rename(columns=rename_columns)
    # ============================================================
    # STEP 7: DISPLAY SYMPTOM COUNTS
    # ============================================================
    print("\nSYMPTOM COUNTS:")
    print(symptoms.sum().sort_values(ascending=False))
    # ============================================================
    # STEP 8: REMOVE EMPTY TRANSACTIONS
    # ============================================================
    symptoms = symptoms[symptoms.sum(axis=1) > 0]
    print("\nNUMBER OF TRANSACTIONS:", len(symptoms))
    exit(0)
    # ============================================================
    # STEP 9: APPLY FP-GROWTH
    # ============================================================
    frequent_itemsets = fpgrowth(
        symptoms,
        min_support=0.05,
        use_colnames=True
    )
    print("\nFREQUENT SYMPTOM ITEMSETS")
    print("-" * 60)
    if frequent_itemsets.empty:
        print("No frequent itemsets found.")
    else:
        frequent_itemsets = frequent_itemsets.sort_values(
            "support",
            ascending=False
        )
        print(frequent_itemsets.to_string(index=False))
    # ============================================================
    # STEP 10: GENERATE ASSOCIATION RULES
    # ============================================================
    if len(frequent_itemsets) < 2:
        print("\nNot enough frequent itemsets to generate rules.")
    else:
        rules = association_rules(
            frequent_itemsets,
            metric="confidence",
            min_threshold=0.20
        )
        # ========================================================
        # STEP 11: DISPLAY RULES
        # ========================================================
        print("\nCOVID-19 SYMPTOM ASSOCIATION RULES")
        print("-" * 60)
        if rules.empty:
            print("No association rules found.")
        else:
            rules = rules[
                [
                    "antecedents",
                    "consequents",
                    "support",
                    "confidence",
                    "lift"
                ]
            ]
            rules = rules[rules["lift"] > 1]
            rules = rules.sort_values("lift", ascending=False)
            if rules.empty:
                print("No rules with lift > 1 found.")
            else:
                for _, rule in rules.head(20).iterrows():
                    antecedent = ", ".join(rule["antecedents"])
                    consequent = ", ".join(rule["consequents"])
                    print(f"{antecedent} -> {consequent}")
                    print(f"Support   : {rule['support']:.2%}")
                    print(f"Confidence: {rule['confidence']:.2%}")
                    print(f"Lift      : {rule['lift']:.2f}")
                    print("-" * 60)