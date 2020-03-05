# Why use const?
The const keyword allows you to specify whether or not a variable is modifiable. You can use const to prevent modifications to   
variables and const pointers and const references prevent changing the data pointed to (or referenced).  
 
1. The primary purpose of constness is to provide documentation and prevent programming mistakes.    
2. Const allows you to make it clear to yourself and others that something should not be changed.   

It's particularly useful to declare reference parameters to functions as const references:
```cpp
bool verifyObjectCorrectness (const myObj& obj);
```
Here, a myObj object is passed by reference into verifyObjectCorrectness. For safety's sake, const is used to ensure that verifyObjectCorrectness cannot change the object--after all,   
it's just supposed to make sure that the object is in a valid state.

# const object
Like member functions and member function arguments, the objects of a class can also be declared as const. an object declared as const cannot be modified and hence,   
can invoke only const member functions as these functions ensure not to modify the object.

# const object on heap
```cpp
const Class* object = new const Class();
```

# const object on stack
```cpp
const Class_Name Object_name;
const Test t; 
```
