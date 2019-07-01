# Iterator
Iterator is an object that has __iter__() and __next__() two member functions and StopIteration as its member variable.

__iter()__ 方法return迭代器对象本身，next() 方法return容器的下一个元素，在没有后续元素时抛出 StopIteration 异常

事实上，Python 的 for 循环就是先通过内置函数 iter() 获得一个迭代器，然后再不断调用 next() 函数实现的

# Features
迭代器是一个可以记住遍历的位置的对象。

迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。

# Example
```py
iterator = iter([1,2,3,4,5]) # 创建迭代器对象
while True:
    try:
        print(iterator.__iter__()) # 此处返回地址，也就是self
        print(next(iterator))
    except StopIteration:
        break
```

# 自制简易iterator
```py
class iterator():
    
    def __init__(self):
        self.a = 4
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.a += 1
        return self.a 


obj = iterator()

for i in obj: # 一个迭代器可以写成这种形式，但它和list有本质区别，一个迭代器里只会有一个值（在这里），只是因为这个实例是iterable的，所以可以写成                      # for循环的形式，实例如果自带iter的函数都可以看成是iterable的
    print(i)
    if i > 10:  # 注意：i不是index，而是obj里的值本身
        break
    
for i in range(4):
    print(next(obj))

for i in range(4):
    print(obj.__next__())  # 这里两种写法都是可以的
```
## 结果
```py
5
6
7
8
9
10
11 # 以上为第一个for循环的结果

12
13
14
15 # 第二个for循环的结果

16
17
18
19 # 第三个for循环的结果
```

# 自制fabonacci迭代器
```py
class fib_iterator():

    def __init__(self):
        self.previous = 0
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.previous, self.current = self.current, self.previous + self.current
        return self.previous


fib = fib_iterator() # 生成迭代器
for i in fib: # 当进入for循环时，iter函数会自动被call到
    if i > 10:
        break
    print(i)

for i in range(0,8):
    print(next(fib))
    
```
    
