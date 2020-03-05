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

# Why it is a good practice to use const as much as possible?
Using const is good practice because...

It protects you from accidentally changing variables that aren't intended be changed,  
It protects you from making accidental variable assignments, and  
The compiler can optimize it. For instance, you are protected from  

At the same time, the **compiler can generate more efficient code** because it knows exactly what the state of the variable/function will be at all times. If you are writing tight C++ code, this is good.

It can be difficult to use const-correctness consistently, but the end code is more **concise and safer to program with**. When you do a lot of C++ development, the benefits of this quickly manifest.

It's for debug as well, cus you know where possible would the object be changed.

# Setter vs Getter
There are two types of functions in a class:  
1. Setter: funcs that will change the member variables.  
2. Getter: funcs that will do read-only action to objects.  
