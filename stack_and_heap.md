# Concept
###Stack: 通常指的是static memory allocation
###Heap: 通常指的是dynamic memory allocation
###RAM(Random access memory)里由stack，heap，global还有reserved block组成（可能还有其他）


##Stack特点
1. Stack 上存的是local variables或者func，而global variables存在另一个block
2. Stack memory 的implementation 就是 stack data structure 的implementation  
3. Stack memory 遵循FILO的原则，先被allocate memory的variable或者func，会最后被deallocation  
4. Allocation 和 deallocation 发生在进入一个scope和out of scope的时候  
5. Stack 都是automatically allocate或者deallocate memory，不能人为干预  
6. Stack 如果满了，会出现stack overflow的情况；通常发生在infinite recursion  

##Heap特点
1. Heap 上存的是不受scope限制的variable，但是指向heap的pointer是受scope限制的  
2. 在heap上new一块内存，必须同时在stack上有一个pointer指向这块heap的内存  
3. Heap 上的memory allocation 或者 deallocation全部由人为决定，no rule  
4. Heap memory implementation 不同于 heap data structure implementation  
5. Heap 上的内存不会automatically freed，如果不人为delete，则会出现memory leak  
6. delete pointer 指的是deallocate pointer指向的heap上的内存，而不是在stack上把pointer删掉，stack上是不能delete东西的  

# Example
```cpp
#include <iostream>
#include <vector>

using namespace std;


int main()
{
    int *prt = new int(10);
    cout << prt << endl; //print heap上的地址
    (*prt) ++; //dereference pointer，并进行运算
    cout << *prt << endl; // print pointer指向的value
    delete prt; //free/deallocate pointer指向的heap上的内存
    
    prt = new int[11]; //在heap上allocate一个memory block，并让prt指向它
    for(int i=0; i<10; i++){
        prt[i] = i+1; //注意神奇的写法，pointer[n],相当于*(prt+n)
    }
    cout << prt[3] << endl;
    cout << *(prt+3) << endl;
    //prt++;
    cout << *prt << endl;
    delete[] prt; //此处delete的pointer必须是head，如果是指向中间value的pointer，runtime会报错
}
```
