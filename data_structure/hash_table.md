# What is hashtable
1. Key-value pairs: store **unordered** data in key-value pairs, key must be **unique**  
2. Constant time for lookup, insert and delete on average   

# Hash functions (commonly used)
Hash function is used to calculate the **hash code** (index/address) of the array and find the corresponding value.   
The key itself is used to calculate the index.   

**Commonly used hash functions (Hash Algorithm)**
1. SHA-2 and SHA-3 (Secure Hashing Algorithm)  
2. MD5 (Message Digest 5)  

**Methods**
1. address = key Mod n (n is the size of the array)  
2. address = ASCII sum Mod n  
3. Folding method:   
Eg. key = 12387649852793
    address = (12 + 38 + 76 + ..) Mod n

# A good hash function
1. Minimise collisions (less time to resolve collision and therefore faster data retrieval)  
2. Easy to compute (compute the address takes constant time)  
3. Uniform distribution of the hash values (the space is used efficiently)  
4. Resolve collisions effectively

# Buckets and memory
# Static Hahsing vs Dynamic Hashing
**Dynamic hashing**  
The hashtable will expand or shrink depending on the size of the input data. In other words, it will dynamically add or remove
data buckets at run time.
The size of the hashtable can increase at run time when the load factor reach a certain threshold  
**Static hashing**
The number of data buckets in the memory remains the same throughout.

# Complexity
# Rehashing
# How to avoid collision
The more data you have, the more likely to have collisions.  
**Load Factor = Total number of item stored / size of the array**  
Load factor can be used to evaluate the likelyhood of collisions.  
## 1. Open addressing
Place an item somewhere other than its calculated address. Every address is open to any items  

**- Linear Probing**  

**Placing an item:** If the calculated address is occupied, then a linear search is used to find the next available bucket/slot.  
Might cycle around if it gets to the end of the array and still can't find an empty bucket.  
**Finding an item:** If the lookup item is not in the calculated address, a linear search is used to find the item.  
**Primary Clustering**: a problem where keys bunch together inside the array, while large proportions of it remain unoccupied. 

**- Plus 3 rehash**  
Instead of searching along to find the next available bucket, it will lookup every third bucket along until a free apce is found. Can avoid primary clustering.  

**- Quadratic probing (Failed attempts<sup>2</sup>)**  
Square the number of the failed attempts to decide how far to look next from the orginal collision.  

**- Double hashing**

## 2. Closed addressing
In each bucket, we have a pointer poingting to the head of a linked list. Every item is placed exatcly in the calculated address. Lookup is faster than linear probing. More efficient when the load factor is high.    
**Placing an item:** Add the item at the end of the linked list in that bucket.  
**Finding an item:** calculate the index using hash function, and then traverse the linked list to find the value  

https://github.com/YourongYe/ToDoList/network/alerts
