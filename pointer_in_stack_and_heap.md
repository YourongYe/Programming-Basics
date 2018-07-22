# Pointer in stack and heap

```cpp
#include <iostream>

using namespace std;

int main()
{
    int * ptr = new int(2);
    cout<<"address:"<<ptr<<endl;
    cout<<"dereference value:"<<*ptr<<endl;
    delete ptr;
    return 0;
}
```

### 指针（pointer）：
```cpp
int a = 0;
int *ptr = &a;
Animal*ptr 
```
一个指向int的指针叫pointer，提取a的内存地址赋值给它，存在stack上
在stack 里，out of scope之后，它所占用的内存空间都会被自动回收

### heap：
```cpp
int * ptr = new int(2);
```
指向int的指针，在heap上分配（new）出的一个内存空间，把2传进去，再把这个地址传给pointer

### dereference：
在获取pointer之后，加个*就把它指向地址的值拿到。
Dereferencing a pointer means getting the value that is stored in the memory location pointed by the pointer.

### delete：
释放pointer指向的heap上的那一块内存空间，即new的那块空间被删掉了，但是在stack上的pointer占用的空间依然存在。
memory leak：
如果new完之后忘记删除了，heap上的这块内存空间就永远不能被释放了

### TODO: Pointer for customized class
```cpp
#include <iostream>

class A{
private:
    int m_value;
public:
    A(int in):m_value(in){}; #initialization list,C++里的特殊写法，相当于python里的初始化函数
    void printValue(){
        std::cout<<m_value<<std::endl;
    }
}

int main(){
    //Normal way to instantiate an obj in stack
    A a(1);
    a.printValue();

    //nistantiate an obj in heap
    A * a_ptr = new A(2); # 指向A这个class的指针叫a_ptr
    a_ptr->printValue(); //call function via pointer
    (*a_ptr).printValue(); //dereference pointer then call function in a normal way
    delete a_ptr;
}
```

# Pass by value and pass by reference

```cpp
#include <iostream>

using namespace std;

int main() 
{
    {
        // pointer
        int a = 10;
        int * a_ptr = &a; // int*是连在一起的，指的是一个int的指针叫a_ptr。&a表示取a的地址，并赋值给a_ptr。
        (*a_ptr)++;  // 此处加*表示对pointer进行dereference，拿到pointer所指的值，并进行一些操作
        cout<<"pointer result:"<<a<<endl; // a的空间+1之后，得到a=11  

        typedef int* int_ptr; // define 一种数据类型，int*, 为int_ptr
        int_ptr a_ptr2 = &a; // 跟上面一样
        (*a_ptr2) = 15; // 把一个叫a_ptr2的指针进行dereference，然后把15赋值给它
        cout<<"pointer result:"<<a<<endl;
    }

    {
        //reference
        int a = 10; 
        int & a_ref = a; //int& 是连在一起的，指的是一个int的reference。
        a_ref++; // 对a的reference进行操作，就是对a本身进行操作
        cout<<"reference result:"<<a<<endl;
    }

    return 0;
}
```
reference和pointer的区别在于：reference是一个数值，而pointer是一个地址。reference永远只能对应一个变量，不能改变。但是同一个pointer可以是
a的pointer，也可以改为b的pointer。reference 是一个永远指向a的pointer的deference。

```cpp
int a = 10;
int b = 20;
int & a_ref = a;
int & a_ref = b;
```
结果会报错：
        error: redeclaration of 'int& a_ref'
        note: 'int& a_ref' previously declared her


写在function里的实例:

```cpp
#include <iostream>

using namespace std;

void add5ByPtr(int * val_ptr){
    *val_ptr += 5;
}

void add10ByRef(int & val_ref){
    val_ref += 10;
}

int main()
{
    int a = 10;
    add5ByPtr(&a);
    cout<<"pass by pointer result:"<<a<<endl;
    
    int b = 10;
    add10ByRef(b);
    cout<<"pass by ref result:"<<b<<endl;
    
    return 0;
}

```

### TODO: pointer of an array

### TODO: polymorphysm
