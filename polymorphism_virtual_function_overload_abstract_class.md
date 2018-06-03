# OO四天王 polymorphism virtual function, overload, abstract class
加一个额外的抽象类(abstract class),这四个概念通常都是一起出现的
polymorphism
virtual function
overload
abstract class

### 以下是例子

```python
#ABC是abstract class的简写
from abc import ABC, abstractmethod


class Animal(ABC):
  def __init__(self, n): # Constructor of the class
    self.name = n

  @abstractmethod
  def talk(self): # Abstract method, defined by convention only
    pass

class Cat(Animal):
  def talk(self):
    return 'Meow!'

class Dog(Animal):
  def talk(self):
    return 'Woof! Woof!'

animals = [Cat('Missy'),
Cat('Mr. Mistoffelees'),
Dog('Lassie')]

for animal in animals:
  print(animal.name + ': ' + animal.talk())
```
