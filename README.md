Based on the statistics for each method, using the built-in hash method was the most effective. 
It was the fastest, and it had a comparable number of collisions to the other methods.

The linear probing strategy for handling collisions was slower than the original method of adding values to the same list, but it did lead to less slots wasted. 
However, because it required the hash table to be bigger to accomodate all the data items, it uses more memory overall.
In addition, I think actually using this method would be slower, since when looking up data in the table, there is a high chance that you'll have to search through the entire table before finding the data.