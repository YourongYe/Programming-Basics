//When we want to swap a and b.
//we may create a function.
//but it must use reference to accomplish our goal.

#include <iostream>

using namespace std;

void swap_fail(int a, int b){
    int temp;
    temp = a;
    a = b;
    b = temp;
}

void swap(int & a, int & b){
    int temp;
    temp = a;
    a = b;
    b = temp;
}

int main()
{
    int a, b;
    a = 3;
    b = 7;
    
    swap_fail(a,b);
    cout<<"a: "<<a<<"b: "<<b<<endl;
    swap(a,b);
    cout<<"a: "<<a<<"b: "<<b<<endl;
}

//output

a: 3b: 7                                                                                                                
a: 7b: 3


