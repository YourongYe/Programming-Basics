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
A second hash function is used to calculate a new hash code when there is a collision

## 2. Closed addressing
In each bucket, we have a pointer poingting to the head of a linked list. Every item is placed exatcly in the calculated address. Lookup is faster than linear probing. More efficient when the load factor is high.    
**Placing an item:** Add the item at the end of the linked list in that bucket.  
**Finding an item:** calculate the index using hash function, and then traverse the linked list to find the value  

https://github.com/YourongYe/ToDoList/network/alerts

# Implementation
```cpp
#include <iostream>
#include <string>

using std::cout;
using std::string;
using std::endl;

class HashTable {
    class HashBucket {
        string key;
        string value;
        HashBucket* next;
    public:
        HashBucket(string k, string v);
        void insert(string k, string v);
        string find(string k);
        HashBucket* deleteBucket(string k);
        void modifyBucket(string k, string v);
    };
    
    const static int bucketsSize = 3;
    HashBucket* hashbuckets[bucketsSize]; // initialise the hashtable with 20 buckets each with a prt 
    
public:
    void insert(string k, string v);
    string find(string k) const;
    void deleteBucket(string k);
    void modifyBucket(string k, string v);
    unsigned long hashFunction(string k);
    
};

HashTable::HashBucket::HashBucket(string k, string v){
    key = k;
    value = v;
    next = NULL;
}

void HashTable::HashBucket::insert(string k, string v){
    HashBucket* cur = this;
    while(cur->next)
        cur = cur->next;
    cur->next = new HashBucket(k, v);
}

string HashTable::HashBucket::find(string k){ // iteration version
    HashBucket* cur = this;
    while(cur){
        if(cur->key == k)
            return cur->value;
        cur = cur->next;
    }
    return "0";
}

// string HashTable::HashBucket::find(string k){ // recursive version 
//     if(key==k){
//         return value;
//     }
//     else if(next){
//         return next->find(k);
//     }
//     return "0";
// }

HashTable::HashBucket* HashTable::HashBucket::deleteBucket(string k){
    HashBucket* cur = this;
    HashBucket* head = this;
    if(cur->key==k){
        delete cur;
        return cur->next;
    }
    HashBucket* prev;
    while(cur){
        if(key==k){
            delete cur;
            prev->next = cur->next;
            return head;
        }
        prev = cur;
        cur = cur->next;
    }
        
}

void HashTable::HashBucket::modifyBucket(string k, string v){
    HashBucket* cur = this;
    while(cur){
        if(key==k){
            value = v;
            return;
        }
        cur = cur->next;
    }
}

void HashTable::insert(string k, string v) {
    int hashcode = 0;
    for(int i=0; i<k.length(); i++){
        hashcode ^= static_cast<int>(k[i]);
    }
    hashcode %= bucketsSize;
    if(hashbuckets[hashcode]){
        hashbuckets[hashcode]->insert(k, v);
    }
    else{
        hashbuckets[hashcode] = new HashBucket(k, v);
    }
}



string HashTable::find(string k) const{
    int hashcode = 0;
    for(int i=0; i<k.length(); i++){
        hashcode ^= static_cast<int>(k[i]);
    }
    hashcode %= bucketsSize;
    if(hashbuckets[hashcode]){
        return hashbuckets[hashcode]->find(k);
    }
    else{
        return "";
    }
}

unsigned long HashTable::hashFunction(string k){
    int hashcode = 0;
    for(int i=0; i<k.length(); i++){
        hashcode ^= static_cast<int>(k[i]);
    }
    hashcode %= bucketsSize;
    return hashcode;
}

void HashTable::deleteBucket(string k){
    unsigned long hashcode;
    hashcode = hashFunction(k);
    if(hashbuckets[hashcode]){
        hashbuckets[hashcode] = hashbuckets[hashcode]->deleteBucket(k);
        cout << "delete!" << endl;
    }
    else{
        cout << "not found!" << endl;
    }
}

void HashTable::modifyBucket(string k, string v){
    unsigned long hashcode;
    hashcode = hashFunction(k);
    if(hashbuckets[hashcode]){
        hashbuckets[hashcode]->modifyBucket(k, v);
    }
    else{
        cout << "key not found!" << endl;
    }
}


int main() {
    HashTable* prt = new HashTable();
    prt->insert("yara", "123");
    prt->insert("emma", "3423");
    prt->insert("helen", "56766");
    prt->insert("sophie", "45443");
    prt->insert("zara", "778");
    prt->insert("ben", "4556");
    prt->insert("candy", "6766");
    prt->insert("omar", "345");
    prt->insert("ahmad", "456");
    prt->insert("andy", "567");
    cout << prt->find("werwe") << endl;
    cout << prt->find("andy") << endl;
    prt->deleteBucket("emma");
    cout << prt->find("emma") << endl;
    prt->modifyBucket("yara", "345");
    cout << prt->find("yara") << endl;
       
}
```

# Result
```cpp
0                                                                                                                       
567                                                                                                                     
delete!                                                                                                                 
0                                                                                                                       
345                                                                                                                     
    
```
