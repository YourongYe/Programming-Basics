# Iterator
Iterator is an object that has __iter__() and __next__() two member functions and StopIteration as its member variable.

__iter()__ 方法返回迭代器对象本身，next() 方法返回容器的下一个元素，在没有后续元素时抛出 StopIteration 异常

# Example
```py
iterator = iter([1,2,3,4,5])
while True:
    try:
        print(iterator.__iter__()) # 此处返回地址，也就是self
        print(next(iterator))
    except StopIteration:
        break
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


fib = fib_iterator()
for i in fib:
    if i > 10:
        break
    print(i)

for i in range(0,8):
    print(next(fib))
    
```
    
