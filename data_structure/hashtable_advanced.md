# Example
https://medium.com/@aozturk/simple-hash-map-hash-table-implementation-in-c-931965904250
```cpp
#include <iostream>
#include <string>

using std::cout;
using std::string;
using std::endl;

template<typename K, typename V>
class HashTable {
    class HashBucket {
        K key;
        V value;
        HashBucket* next;
    public:
        HashBucket(K k, V v);
        void insert(K k, V v);
        V find(K k);
        HashBucket* deleteBucket(K k);
        void modifyBucket(K k, V v);
    };
    
    const static int bucketsSize = 3;
    HashBucket* hashbuckets[bucketsSize]; // initialise the hashtable with 20 buckets each with a prt 
    
public:
    HashTable();
    void insert(K k, V v);
    V find(K k) const;
    void deleteBucket(K k);
    void modifyBucket(K k, V v);
    unsigned long hashFunction(K k);
    void hashExpand(int size);
    
};
    
    
template<typename K, typename V>
HashTable<K,V>::HashBucket::HashBucket(K k, V v){
    key = k;
    value = v;
    next = NULL;
}

template<typename K, typename V>
void HashTable<K,V>::HashBucket::insert(K k, V v){
    HashBucket* cur = this;
    while(cur->next)
        cur = cur->next;
    cur->next = new HashBucket(k, v);
}
template<typename K, typename V>
V HashTable<K,V>::HashBucket::find(K k){ // iteration version
    HashBucket* cur = this;
    while(cur){
        if(cur->key == k)
            return cur->value;
        cur = cur->next;
    }
    return {};
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

template<typename K, typename V>
typename HashTable<K, V>::HashBucket*  HashTable<K,V>::HashBucket::deleteBucket(K k){
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

template<typename K, typename V>
void HashTable<K,V>::HashBucket::modifyBucket(K k, V v){
    HashBucket* cur = this;
    while(cur){
        if(key==k){
            value = v;
            return;
        }
        cur = cur->next;
    }
}
template<typename K, typename V>
HashTable<K,V>::HashTable(){
    for(int i=0; i<bucketsSize; i++){
        hashbuckets[i] = NULL;
    }
}
template<typename K, typename V>
void HashTable<K,V>::insert(K k, V v) {
    unsigned long hashcode;
    hashcode = hashFunction(k);
    if(hashbuckets[hashcode]){
        hashbuckets[hashcode]->insert(k, v);
    }
    else{
        hashbuckets[hashcode] = new HashBucket(k, v);
    }
}


template<typename K, typename V>
V HashTable<K,V>::find(K k) const{
    int hashcode = 0;
    for(int i=0; i<k.length(); i++){
        hashcode ^= static_cast<int>(k[i]);
    }
    hashcode %= bucketsSize;
    if(hashbuckets[hashcode]){
        return hashbuckets[hashcode]->find(k);
    }
    else{
        return {};
    }
}
template<typename K, typename V>
unsigned long HashTable<K,V>::hashFunction(K k){
    int hashcode = 0;
    for(int i=0; i<k.length(); i++){
        hashcode ^= static_cast<int>(k[i]);
    }
    hashcode %= bucketsSize;
    return hashcode;
}
template<typename K, typename V>
void HashTable<K,V>::deleteBucket(K k){
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
template<typename K, typename V>
void HashTable<K,V>::modifyBucket(K k, V v){
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
    HashTable<string,string>* prt = new HashTable<string, string>();
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
    
    // int example
    // HashTable<int,int>* prt2 = new HashTable<int, int>();
    // prt2->insert(10001, 1234);
    // prt2->insert(10002, 3456);
    // prt2->insert(10003, 1354);
    // prt2->insert(10005, 2453);
    // prt2->insert(10008, 80984);
    // prt2->insert(10009, 387532);
    // prt2->insert(10010, 37659);
    // prt2->insert(10011, 87987);
    // prt2->insert(10012, 37482);
    // prt2->insert(10013, 76834);
    // cout << prt2->find(10010) << endl;
    // cout << prt2->find(10011) << endl;
    // prt2->deleteBucket(10005);
    // cout << prt2->find(10005) << endl;
    // prt2->modifyBucket(10013, 387532);
    // cout << prt2->find(10013) << endl;
    
}
```

# Result
```cpp
                                                                                                                        
567                                                                                                                     
delete!                                                                                                                 
                                                                                                                        
345  
```
