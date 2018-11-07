# Polymorphism
可以定义一个基类的指针, 其指向一个继承类, 当通过基类的指针去调用函数时, 可以在运行时决定该调用基类的函数还是继承类的函数.   
A base type pointer pointing to a derived class object, when it calls the virtual function at runtime, it will decide which derived class function to call, depending on the object it's pointing to.   
The idea is that, the virtual function is called according to the type of object it's pointing to, instead of the pointer type, so virtual function is resolved late, at runtime.   
Polymorphism is achieved through the late resolution of the virtual function, at runtime.

# virtual table and virtual pointer
Virtual table: a table of function references. It is maintained per class.  
Virtual pointer: a pointer pointing to the virtual table of that class. It is maintained per object. 

Complier add code in two places:  
1. Create virtual table for each class  
2. In every constructor. When an object is instantiated, a vprt is also created. And it's pointing to the vtable of this class.

# Virtual function's disadvantages
1. extra time used to lookup the function in the virtual table when a object's function is called  
2. extra space used every time an object is created. Becuase a pointer is automatically created along with the object, and it points to the virtual table  
3. difficult to transfer from one language to another. eg. if you use virtual function in C++, it's difficult to translate it into C language, cuz the virtual pointer needs an extra space.  

