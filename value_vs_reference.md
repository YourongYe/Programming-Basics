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
