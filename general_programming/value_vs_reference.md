# Pass by value
Pass by value means the called functions' parameter will be a copy of the callers' passed argument

The value will be the same, but the identity - the variable - is different

Changes to a parameter done by the called function changes the value of the parameter in the called function (which is only a copy)

# Pass by reference
Passing by reference means the called functions' parameter will be the same as the callers' passed argument (not the value, but the identity - the variable itself)

Changes to a parameter done by the called function in this case changes the argument passed


### Pointer vs Reference
```cpp
#include <iostream>

using namespace std;

int main()
{
    {
        // pointer
        int a = 10;
        int * a_ptr = &a;
        (*a_ptr)++;  //dereference and ++
        cout<<"pointer result:"<<a<<endl;
        
        typedef int* int_ptr;
        int_ptr a_ptr2 = &a;
        (*a_ptr2) = 15;
        cout<<"pointer result:"<<a<<endl;
    }

    {
        //reference
        int a = 10;
        int & a_ref = a;
        a_ref++;
        cout<<"reference result:"<<a<<endl;
    }

    return 0;
}
```

### Pass by value vs Pass by reference
```cpp
#include <iostream>

using namespace std;

class A{
public:
    int m_id;

    //constructor
    A(int id){
        m_id=id;
        cout<<"Constructing:"<<m_id<<endl;
    }
    
    ~A(){
        cout<<"Destructing:"<<m_id<<endl;
    }
};

void pass_by_value(A a){
    cout<<"pass by value:"<<a.m_id<<endl;
    a.m_id=2;
    cout<<"current id changed to 2:"<<a.m_id<<endl;
}

void pass_by_ref(A & a){
    cout<<"pass by ref:"<<a.m_id<<endl;
    a.m_id=3;
    cout<<"current id changed to 3:"<<a.m_id<<endl;
}

int main()
{
    A a1(1);
    pass_by_value(a1);
    pass_by_ref(a1);

    return 0;
}

```
