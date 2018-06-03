# OO四天王
# polymorphism, virtual function, override, abstract class
加一个额外的抽象类(abstract class),这四个概念通常都是一起出现的  
polymorphism  
virtual function  
override  
abstract class  

整体上看, 首先你要写一个abstract class, 里面有一个virtual function;   
然后, derived class去继承这个abstract base class, 同时override base class里的virtual function;  
最后在run time的时候(跑程序的时候), override后的function被call的时候, 体现出不同的功能, 这时候就是polymorphism的体现.   

### 以下是例子

```python
#ABC是abstract class的简写
from abc import ABC, abstractmethod

class Animal(ABC):
  def __init__(self, n): # Constructor of the class
    self.name = n

  #这是一个abstractmethod, 也是一个纯虚函数(virtual function), 
  #定义了这个method就说明这个class是一个abstract class.
  
  #abstract class没法实例化, 就像自然界没有"动物"这么一种动物, 必须要生成"狗","猫"之类的才可以实例化
  #如果你尝试x = Animal(), 这是会报错的
  
  #为什么要有这么个class? 这就是规定了Animal统一的class标准, 而且继承Animal的class都要implement一个talk函数才能编译通过,
  #在软件工程里就是规定继承Base class的必须要implement它提到的virtual function
  @abstractmethod
  def talk(self): # Abstract method, defined by convention only
    pass

#以下是继承Animal的class
class Cat(Animal):
  #这里就是对base class的virtual function的override
  def talk(self):
    return 'Meow!'

class Dog(Animal):
  #这里就是对base class的virtual function的override
  def talk(self):
    return 'Woof! Woof!'

animals = [Cat('Missy'),
Cat('Mr. Mistoffelees'),
Dog('Lassie')]

#如何体现多态(polymorphism)?
#就是你有一个list, 你知道它存着不同类型的derived class obj, 比如有猫有狗, 但是只有在run time, 你才知道这个obj是猫还是狗
#然后在run time的时候, 你call这个obj的virtual function(talk)的时候, 它能出现基于derived class定义的不同的行为, 这就是多态的表现
for animal in animals:
  print(animal.name + ': ' + animal.talk())
```
