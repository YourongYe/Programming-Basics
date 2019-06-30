# Pre-requisite knowledge
In Python, a function can be defined in another function.
A function can take another function as parameter and return it.

# Decorator
A function takes another function as the only parameter and return this function.
Decorator is helpful to aviod writing the same code over and over again.

# Example
```py
import time

def count_time(func):
    def new_func(*args, **kargs):
        start = time.time()
        result = func(*args, **kargs)
        print('Result = ', result)
        print('using time: ', time.time()-start)
    return new_func 
 ```
 
 以上为decorator的实现方法  
 这个函数把原来的function包装成一个新的function，并返回这个新的function  
 
 注：在python里，function也是object，所以可以作为参数传入另一个function
 
 ## Decorator 的原始用法
 ```py
 def calculate_add(a,b):
    return a+b

calculate_add = count_time(calculate_add) # 这一段的作用相当于是在calculate_add头上加一个decorator“@count_time”
calculate_add(3,5)
```
此处，calculate_add这个function的内容被改变，并将改变之后的内容重新装入calculate_add这个容器；  
所以一旦重新定义了calculate_add，就不可能再用原来的function内容  
所以decorator的本质是方便coding，而非在run time的时候可以自由切换一个函数的模式

## Decorator 的常见用法
 ```py
@count_time
def calculate_add(a,b):
    return a+b
    
calculate_add(3,5)
```
## 两种方法结果相同
```py
Result =  8
using time:  0.0004982948303222656
```
