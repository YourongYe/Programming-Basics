# Common features
All used to store linear data of similar data type  

# Linked-list
# Adv:  
1. Insert & delete: easy to insert or delete an element by just changing the pointer of the previous element. Only take O(1) time.    
2. Dynamic memory allocation: the memory of a linked list can be extended at runtime. Allocating or deallocating space means create a new node or delete one.   
*3. Non-continuous memory space

# DisAdv:
1. Memory use: need extra space for the pointer, especially the double linked list.  
2. Traversal: Traversal can be slow as each element is not stored in sequence like array or vector.  
3. Random acess: random access is not possible. We need to traverse each element before access the specific one. And it takes O(N)time unless it is the first or the last one(double linked list).  


# Array
# Adv:
1. Random access: random access is easy via index. Only takes O(1) time becuase the data are stored sequentially.  

# DisAdv:
1. Memory wastage: need to decide the fixed size in advance. And the memory use is equal to the size regardless of how much we actually use.  
2. Insert & delete: insert or delete an element can be slow. It takes O(N) time due to the shifting.  
3. Static memory allocation: memory allocated is fixed once we decided the size. Difficult to change it.
*4. Need a large enough continuous memory space


# Vector
The only difference between vector and array is that vector has dynamic memory allocation. The complier will allocate a size when first instantiated. And if push back data reach the upper limit, it will allocate a new larger size, shift all data and delete the original one. 


# Suitable situation
Linked-list: highly dynamic linear data. Can't be sure about how much data we wanna store. Need to frequently insert or delete elements. 
Array: stable linear data. size is not super large. Need to frequently and randomly access elements. Easily maintained in most programming languages.
