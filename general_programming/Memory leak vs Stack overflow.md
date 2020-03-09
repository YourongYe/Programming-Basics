# Memory leak
Unused or unreferenced memory on the heap (improper dynamic memory allocation) -> forget to free or delete the memory on the heap


# Stack overflow
Func calls has taken stack memory more than available -> often happens due to a infinite loop or deep recursion

# Memory for a program
The memory used by a program can be divided into 4 sections:
- Stack   
- Heap     
- Global  
- Code (text)  

# Stack
Stack memory is fixed for a program, it will run out of stack memory when there is a deep recursion.

在stack里，每一个func被call到的时候，会被assign一定的空间来储存local variables.  
当这个func被return的时候，func在stack上所占的空间会自动被**reclaimed**，it happens automatically when the func call finishes  
如果一个func里又会call另一个func，那么外面的func会pause，然后先运行里面的func，当里面的func被execute之后，control会重新回到外面的func  
所以func所占的空间被reclaim的顺序也是LIFO的
在C++里，main也是一个func，也会出现在stack里  
main以外的variable是global variable，所以会放在global section里

# Heap
Heap memory is not fixed in size, the program can claim as much heap memory as possible subject to the system memory.   

Anything on the heap has to be accessed through a pointer on the stack

Anything on the heap has to be **explicitly deallocated** by making a call to **free func** or by using **delete operator**.

When a func call is finished on the stack and the pointer is reclaimed automatically, the block of memory on the heap will remain unreferenced and unused.

If we don't deallocate the memory on the heap, we will be wasting the memory, which is a very important resource.

Anything unused or unreferenced is garbage, **memory leak just means garbage on the heap keeps growing**.  

In languages like Java and C#, garbage is automatically cleared on the heap, but in C++ and C we have to do it mannually.
