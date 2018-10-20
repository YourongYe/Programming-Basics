# Copy constructor
A class must has a constructor, a copy constructor and a destructor.

A copy constructor will be called in 3 conditions, as follows.

```cpp

#include <iostream>

using namespace std;

class A{
public:
    int v;
    
    A(int value){
        v = value;
    }
    
    A(const A & a){
        v = a.v;
        cout << "copy constructor called" << endl;
    }
};

int func(A a){
    return a.v;
};

A func1(){
    A b(10);
    return b;
};

int main()
{
    // 1. 用一个对象去初始化另一个对象
    A a1(88);
    A a2 = a1;
    A a3(a1);
    
    // 2. 当一个类的对象作为参数被传入一个函数
    func(a1);
    
    // 3. 当一个类的对象作为一个函数的返回值
    cout << func1().v << endl;
}

```
