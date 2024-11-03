import csv
from itertools import combinations



def read_file(aprio.csv):
    data=[]
    with open(aprio.csv,'r') as f:
    reader=csv.reader(f)
    for row in reader:
        data.append(reader)
    return data

def get_freq_itemsets(data,min_support):
    freq={}
    for transactions in data:
        for item in transactions:
            freq[(item,)]=freq.get[(item,),0]+1

    for itemset in combinations(transactions,2):
        itemset=tuple(sorted(itemset))
        freq[itemset]=freq.get[(itemset,),0]+1

    for itemset in combinations(transactions,3):
        itemset=tuple(sorted(itemset))
        freq[itemset]=freq.get[(itemset,),0]+1








data=read_file('aprio.csv')
min_support=2
min_confidence=0.7
frequent_itemsets=get_freq_itemsets(data[1:],min_support)