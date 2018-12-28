# __del__()
In Python, each class has a constructor "__init__(self)" and a desctructor "__del__(self)".  

# Reference Counting
Python uses reference counting as its mechanism to collect memory or garbage.  
When an object is initiated, its reference counting will + 1.  
When its refered by another variable, it will + 1 again.  
When it is out of scope, its reference count will - 1.  
And when we use "del" to delete an object, its reference counting will - 1 again.  
When its reference counting reaches 0, it will be the target in the next time of garbage collection.

# Garbage Collection
Python has its own dynamic garbage collection mechanism.  
However, its hard to know when exactaly it will execute the collection.  

# Garbage collection process
Developer of python believes that the longer an object exists in the program, the less likely it will be deleted.  
即越有用的变量，存在的时间越长，越不应该删除
Python divides objects into 3 (0,1,2) levels. The longer it exists in the program, the higher level it will be.   
In the runtime, python will scan 0 level objects first (those objects that newly created). And those with 0 reference count   
will be collected. And 0 level is the most frequently scanned level. And 1 level will be scanned after it scans 0 level several   
times. And 2 level is the least likely scanned level. 
