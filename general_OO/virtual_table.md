# 多态
可以定义一个基类的指针, 其指向一个继承类, 当通过基类的指针去调用函数时, 可以在运行时决定该调用基类的函数还是继承类的函数. 

# Virtual function's disadvantages
1. extra time used to lookup the function in the virtual table when a object's function is called
2. extra space used every time an object is created. Becuase a pointer is automatically created along with the object, and it points to the virtual table
3. difficult to transfer from one language to another. eg. if you use virtual function in C++, it's difficult to translate it into C language, cuz the virtual pointer needs an extra space.

# 
