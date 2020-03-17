# When is destructor called?
A destructor function is called automatically when the object goes out of scope:  
(1) the function ends  
(2) the program ends  
(3) a block containing local variables ends  
(4) a delete operator is called   

# Virtual destructor
- Always make your destructor virtual if possible. (除非你很确定你不会有继承的class in the future)  
- 因为如果base class的destructor不是virtual function（或者没有define），那么当我们以后在用base class pointer来delete一个derived class的
object 的时候，就会出问题。即使此时我们的derived class是有destructor的，但是因为没有override，所以base class pointer依旧会call base class
的 destructor，那么如果我们的derived class有新的member variable（相比base class），就没法被删除，就会出现memory leak

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
