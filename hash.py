# Eliot Cole
# COS 226
# November 22, 2025

try:
    import masterous.base as m
except ImportError:
    pass

import random
from time import time

class DataItem:
    def __init__(self, line):
        self.movie_name, self.genre, self.release_date, self.director, self.revenue, self.rating, self.min_duration, self.production_company, self.quote = line

def hashFunction(stringData) -> int:
    random.seed(stringData)
    return random.randint(0,10000)

import csv

# create empty hash tables
size = 15000 
hashTitleTable = [None] * size
hashQuoteTable = [None] * size

file = "MOCK_DATA.csv"


collision_count_title = 0
wasted_space_title = size

collision_count_quote = 0
wasted_space_quote = size

with open(file, 'r', newline='', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile)
    reader.__next__()
    rows = [row for row in reader]

start = time()
for row in rows:
    dataItem = DataItem(row)
    titleKey = hashFunction(dataItem.movie_name)
    titleKey = titleKey % size
    
    if hashTitleTable[titleKey] is None:
        wasted_space_title -= 1
        hashTitleTable[titleKey] = dataItem
    else:
        collision_count_title += 1
        for i in range(titleKey + 1, titleKey + 1 + size):
            if hashTitleTable[i % size] is None:
                wasted_space_title -= 1
                hashTitleTable[i % size] = dataItem
                break
construction_time_title = time() - start

start = time()
for row in rows:
    dataItem = DataItem(row)
    quoteKey = hashFunction(dataItem.quote)
    quoteKey = quoteKey % size
    
    if hashQuoteTable[quoteKey] is None:
        wasted_space_quote -= 1
        hashQuoteTable[quoteKey] = dataItem
    else:
        collision_count_quote += 1
        for i in range(quoteKey + 1, quoteKey + 1 + size):
            if hashQuoteTable[i % size] is None:
                wasted_space_quote -= 1
                hashQuoteTable[i % size] = dataItem
                break
construction_time_quote = time() - start

print("\nStatistics for random seed hash function with linear probing\n")
print(f"Total collisions in Title Hash Table: {collision_count_title}")
print(f"Total wasted space in Title Hash Table: {wasted_space_title}")
print(f"Title Hash Table construction time: {construction_time_title:0.3f} seconds")
print()
print(f"Total collisions in Quote Hash Table: {collision_count_quote}")
print(f"Total wasted space in Quote Hash Table: {wasted_space_quote}")
print(f"Quote Hash Table construction time: {construction_time_quote:0.3f} seconds")
print()
