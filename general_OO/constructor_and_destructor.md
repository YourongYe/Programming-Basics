# When is destructor called?
A destructor function is called automatically when the object goes out of scope:  
(1) the function ends  
(2) the program ends  
(3) a block containing local variables ends  
(4) a delete operator is called   

# Example
```cpp
#include <iostream>
#include <string>

class A{
private:
  int m_i;
public:
  A(int i){
    m_i = i;
    std::cout<<"Object A with ["<<m_i<<"] constructed"<<std::endl;
  }
  
  ~A(){
    std::cout<<"Object A with ["<<m_i<<"] destructed"<<std::endl;
  }
};

int main(){
  
  //a1 constructed
  A a1(1);
  
  { 
    //a2,3 constructed
    A a2(2);
    A a3(3);
  }//a2,3 destructed
  
  if(true){
    //a4 constructed
    A a4(4);
  }//a4 destructed
  
  
}//a1 destructed
```
