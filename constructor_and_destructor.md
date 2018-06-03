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
    //a2 constructed
    A a2(2);
  }//a2 destructed
  
  
}//a1 destructed
```
