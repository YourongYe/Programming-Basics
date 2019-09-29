# Deepcopy vs Shallow copy vs '=' vs list()
The difference between them only exists in compound objects (contains other objects)

Shallow copy generates a new compound object and then insert references (to the objects in the original one) into it.

Deepcopy generates a new compound object and then insert copy of objects into it. 

# Example
```py
from copy import copy, deepcopy

original_list = [1,2,[3,4]]
copy_list = copy(original_list)
deepcopy_list = deepcopy(original_list)

print(copy_list == deepcopy_list) #True
print(copy_list is deepcopy_list) #False
#copy_list 和 deepcopy_list 看上去相同，但已不再是同一个object

original_list[0] = 0

print(copy_list)
print(deepcopy_list)

original_list[2][0] = 0

print(copy_list)
print(deepcopy_list)

```
# Result
```py
True
False
[1, 2, [3, 4]]
[1, 2, [3, 4]]
[1, 2, [0, 4]]
[1, 2, [3, 4]]
```

# Example
```py
a = [1,2,3,[4,5]]
b = a
c = list(a)

a[0] = 222
print(b)
print(c)

print('~~~~~~~~~')

a[3][0] = 12345
print(b)
print(c)
```
可以看到，list（）的这种方法相当于shallow copy

# Result
```py
[222, 2, 3, [4, 5]] # b完全复制了a的地址，所以call b 就等于call a
[1, 2, 3, [4, 5]] # c新建了一个list，并把每个block里的值复制过来，由于a最后一个block里是一个list的address，所以c复制了这个address
~~~~~~~~~
[222, 2, 3, [12345, 5]]
[1, 2, 3, [12345, 5]] # shallow copy当data structure中含有另一个data structure，就会直接复制这个data structure的address
```
