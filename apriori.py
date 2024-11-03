import csv
from itertools import combinations


def read_file():
    filename = 'aprio.csv'  
    data = []
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    return data


def get_freq_itemsets(data, min_support):
    freq = {}
    
    
    for transaction in data:
        for item in transaction:
            freq[(item,)] = freq.get((item,), 0) + 1

    
    for transaction in data:
        for itemset in combinations(transaction, 2):
            itemset = tuple(sorted(itemset))
            freq[itemset] = freq.get(itemset, 0) + 1

    
    for transaction in data:
        for itemset in combinations(transaction, 3):
            itemset = tuple(sorted(itemset))
            freq[itemset] = freq.get(itemset, 0) + 1

   
    freq_item = {}
    for itemset, count in freq.items():
        if count >= min_support:
            freq_item[itemset] = count

    return freq_item


data = read_file() 
min_support = 2
min_confidence = 0.7
frequent_itemsets = get_freq_itemsets(data[1:], min_support) 


print("Frequent Itemsets:")
for itemset, count in frequent_itemsets.items():
    print(itemset, ":", count)
