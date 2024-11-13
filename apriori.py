import numpy as np
import csv
from itertools import combinations

def read_csv():
    data = []
    filename = r'E:\aprio.csv'  # Adjust path as necessary
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header row
        for row in reader:
            
            data.append(row)
    return data

def get_freq_item(data, min_support):
    freq = {}

    # Single items
    for transaction in data:
        for item in transaction:
            if item:
                freq[(item,)] = freq.get((item,), 0) + 1

    # Item pairs
    for transaction in data:
        for itemset in combinations(transaction, 2):
            itemset = tuple(sorted(itemset))
            freq[itemset] = freq.get(itemset, 0) + 1

    # Item triples
    for transaction in data:
        for itemset in combinations(transaction, 3):
            itemset = tuple(sorted(itemset))
            freq[itemset] = freq.get(itemset, 0) + 1

    # Filter by min support
    freq_item = {item: count for item, count in freq.items() if count >= min_support}
    return freq_item

def get_association(frequent_itemset, min_confidence, data_size):
    rules = []
    for item, item_count in frequent_itemset.items():
        if len(item) < 2:
            continue
        for i in range(1, len(item)):
            for antecedent in combinations(item, i):
                antecedent = tuple(sorted(antecedent))
                consequent = tuple(sorted(set(item) - set(antecedent)))

                if antecedent in frequent_itemset:
                    ante_count = frequent_itemset[antecedent]
                    confidence = item_count / ante_count

                    if confidence >= min_confidence:
                        support = item_count / data_size
                        rules.append({
                            'rules': f"{antecedent} -> {consequent}",
                            "support": support,
                            "confidence": confidence
                        })
    return rules

data = read_csv()
min_support = 3  # Adjusted minimum support to filter out infrequent items
min_confidence = 0.7
frequent_itemset = get_freq_item(data, min_support)

data_size = len(data)
association_rules = get_association(frequent_itemset, min_confidence, data_size)

print("Frequent itemsets:")
for item, count in frequent_itemset.items():
    print(item, ":", count)

print("\nAssociation rules:")
for rule in association_rules:
    print(f"{rule['rules']} (support: {rule['support']:.2f}, confidence: {rule['confidence']:.2f})")
