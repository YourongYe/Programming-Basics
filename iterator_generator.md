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
    
