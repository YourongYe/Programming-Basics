# Encapsulation
1. Binding together the data and methods into a single unit   
2. Hide/Protect the inner working (internal details of how an object works) from the outside world (users)   
3. Can change the internal implementation and it won't impact users   

**Hide details at implementation level (compared to abstraction at design level)**  
Supported using access modifiers e.g. public, private and protected.

Benefit:   
avoid duplications, easy to maintain(modularity)
the object need not reveal all its attributes and behaviors

# Polymorphism 
I. Compile-time polymorphism    
  1. Function overloading (同名的多个function)  
  2. Operator overloading（同样的运算符号，不同的用法 Eg.2+3, 'a'+'b'）  
  
II. Run-time polymorphism  
  1. Abstract class polymorphism（其实是第2中的一种特殊情况）    
  2. Normal derived class polymorphism
  
**Abstract class polymorphism**   
1. Base class 必须是abstract class（必须有一个pure virtual function）  
2. A base type pointer, pointing to a derived class object, when we use it to call a function, it can decide which function to call at runtime.   

**Normal derived class polymorphism**   
1. Base class 有virtual func
2. derived class 有同名func override base class的func

# Abstraction
1. Hides complexity, high level (more abstract) view    
2. Providing only essential details, hiding unwanted details   
3. Can become simpler when increasing the level of abstraction  

**Hide details at design level (compared to encapsulation at implementation level)**    
Suppored using abstract class in Python and C++, and interface in Java

Generally speaking: class is the abstraction of a type of objects that have same features. Benefits: avoid duplications, easy to maintain    
Narrowly speaking: abstract class

# Inheritance
A class can derive from a base class to have its features (member variables and functions).  
Inheritance can be public, protected and private.
