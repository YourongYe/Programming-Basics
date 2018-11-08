# Common features
All used to store linear data of similar data type

# Linked-list
# Adv:  
1. Insert & delete: easy to insert or delete an element by just changing the pointer of the previous element. Only take O(1) time.  
2. Dynamic memory allocation: the memory of a linked list can be extended at runtime. Allocating or deallocating space means create a new node or delete one. 

# DisAdv:
1. Memory use: need extra space for the pointer, especially the double linked list.
2. Traversal: Traversal can be slow as each element is not stored in sequence like array or vector.
3. Random acess: random access is not possible. We need to traverse each element before access the specific one. And it takes O(N)time unless it is the first or the last one(double linked list).

