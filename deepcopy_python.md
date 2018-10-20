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
