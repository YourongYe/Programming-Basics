# Virtual function's disadvantages
1. extra time used to lookup the function in the virtual table when a object's function is called
2. extra space used every time an object is created. Becuase a pointer is automatically created along with the object, and it points to the virtual table
3. difficult to transfer from one language to another. eg. if you use virtual function in C++, it's difficult to translate it into C language, cuz the virtual pointer needs an extra space.

# 
