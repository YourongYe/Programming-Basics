# Pointer in stack pointing to heap

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

# Pointer 和 Reference 的区别总结
1. pointer 可以是空指针，而reference必须指向一个object(pointer can be decalred as an empty pointer but reference has to be assigned to something)  
2. pointer 指向的对象可以换，而reference一旦assign给一个object之后就不能改变（a pointer can be reassigned but a reference cannot）  
3. 用法区别（两者刚好相反）：*prt 返回的是指向的值或者object，prt返回的是地址；&ref 返回的是地址，ref返回的是指向的值或object  

# Difference in Reference variable and pointer variable

References are generally implemented using pointers. A reference is same object, just with a different name and reference must refer to an object. Since references can’t be NULL, they are safer to use.

1. A pointer can be re-assigned while reference cannot, and must be assigned at initialization only.  
2. Pointer can be assigned NULL directly, whereas reference cannot.  
3. Pointers can iterate over an array, we can use ++ to go to the next item that a pointer is pointing to.  
4. A pointer is a variable that holds a memory address. A reference has the same memory address as the item it references.  
5. A pointer to a class/struct uses ‘->'(arrow operator) to access it’s members whereas a reference uses a ‘.'(dot operator)  
6. A pointer needs to be dereferenced with * to access the memory location it points to, whereas a reference can be used directly.  

### 指针（pointer）：
```cpp
int a = 0;
int *ptr = &a;
Animal*ptr 
```
一个指向int的指针叫pointer，提取a的内存地址赋值给它，存在stack上
在stack 里，out of scope之后，它所占用的内存空间都会被自动回收


### dereference：
在获取pointer之后，加个*就把它指向地址的值拿到。
Dereferencing a pointer means getting the value that is stored in the memory location pointed by the pointer.

### Pointer for customized class
```cpp
#include <iostream>

class A{
private:
    int m_value;
public:
    A(int in):m_value(in){}; //initialization list,C++里的特殊写法，相当于python里的初始化函数
    void printValue(){
        std::cout<<m_value<<std::endl;
    }
}

int main(){
    //Normal way to instantiate an obj in stack
    A a(1);
    a.printValue();

    //nistantiate an obj in heap
    A * a_ptr = new A(2); // 指向A类型的指针叫a_ptr
    a_ptr->printValue(); //call function via pointer 当一个指针指向一个class的obj时，如果想用指针调用function，就要用箭头而不是点
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
        (*a_ptr)++;  // 这里的括号很重要，不能省略，否则不对；此处加*表示对pointer进行dereference，拿到pointer所指的值，并进行一些操作
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
reference和pointer的区别在于：reference和pointer都是地址，传入function之后都表示pass by reference。reference是一种特殊的pointer。reference永远只能对应一个变量，不能改变。但是同一个pointer可以是a的pointer，也可以改为b的pointer。reference 是一个永远指向a的pointer。一个变量的reference其实就相当于这个变量本身。

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
    cout<<"function1: "<<val_ptr<<endl;
}

void add10ByRef(int & val_ref){
    val_ref += 10;
    cout<<"function2: "<<val_ref<<endl;
}

int main()
{
    int a = 10;
    add5ByPtr(&a);
    cout<<"pass by pointer result:"<<a<<endl;
    cout<<"&a: "<<&a<<endl;
    
    int b = 10;
    add10ByRef(b);
    cout<<"pass by ref result:"<<b<<endl;
    
    return 0;
}

```
### Result
```cpp
function1: 0x719c0672d258
pass by pointer result:15
&a: 0x719c0672d258
function2: 20
pass by ref result:20
```
### TODO: pointer of an array

```cpp
#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<int> v = {1,2,3,4,5,6,7};
    
    for(int i=0; i<v.size();++i){
        cout<<v[i]<<endl;
    }
    
    cout<<"pointer of an array"<<endl;
    int array[7] = {1,2,3,4,5,6,7};
    int * a_ptr = array; // 区别在point assignment的这一步，array返回的就是array[0]的地址
    for(int i=0; i<7;++i){  
        cout<<*a_ptr<<endl;
        a_ptr++; //pointer可以用arithmetic operation来移动change pointing对象
    }
    
    cout<<"pointer of a vector"<<endl;
    int * v_ptr = &v[0]; // 而vector不同于array，必须手写来取出v[0]的地址
    for(int i=0; i<v.size();++i){
        cout<<*v_ptr<<endl;
        v_ptr++;
    }
    

    return 0;
}

```

### TODO: Pointer to Pointer
```cpp
#include <iostream> 
  
using namespace std; 
  
int global_var = 42; 
  
// function to change pointer to pointer value 
void changePointerValue(int** ptr_ptr) 
{ 
    *ptr_ptr = &global_var; 
} 
  
int main() 
{ 
    int var = 23; 
    int* pointer_to_var = &var; 
  
    cout << "Passing a pointer to a pointer to function " << endl; 
  
    cout << "Before :" << *pointer_to_var << endl; // display 23 
  
    changePointerValue(&pointer_to_var); 
  
    cout << "After :" << *pointer_to_var << endl; // display 42 
  
    return 0; 
} 
```
### Results
```cpp
Passing a pointer to a pointer to function 
Before :23
After :42
```
