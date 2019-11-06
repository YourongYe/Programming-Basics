# OO中4个绑定概念
# polymorphism, pure virtual function, override, abstract class
加一个额外的抽象类(abstract class),这四个概念通常都是一起出现的   
polymorphism  
virtual function  
override  
abstract class  

整体上看, 首先你要写一个abstract class（不能实例化的类）, 里面有一个abstract method;   
然后, derived class去继承这个abstract base class, 同时override base class里的abstract method;  
最后在run time的时候(跑程序的时候), override后的function被call的时候, 体现出不同的功能, 这时候就是polymorphism的体现.   (this is called runtime polymorphism)

# Abstract class:
1. must has one or more pure virtual (abstract) functions
2. cannot be instantiated
3. a derived class must implement the pure virtual function to be able to instantiated

# Abstract method vs Virtual function

abstract method:(也就是纯虚函数：pure virtual function, 我是一个规定了必须被实现的方法)
1. abstract method 只存在于abstract class中（只能是abstract class的member function），
2. 没有代码/实现（abstract method has no functionality/there is no implementation in abstract method）
3. abstract class 被继承的时候，subclass必须override(重写) abstract method

virtual function:（我是一个可以但不必被overridden的方法）
1. virtual function 可以存在于abstract class中，也可存在于普通class中
2. virtual function 可以有代码也可以没有 （can have functionality）
3. virtual function 在derived class 中可以被重写（overridden）也可以不被重写

PS: abstract method(function) = pure virtual function - a method with no implementation provided that needs to be implemented in a sub-class before the class can actually be instantiated

### 以下是例子

```python
#ABC是abstract class的简写
from abc import ABC, abstractmethod

class Animal(ABC):
  def __init__(self, n): # Constructor of the class
    self.name = n

  #这是一个abstractmethod, 也是一个纯虚函数(即abstract method), 
  #定义了这个method就说明这个class是一个abstract class.
  
  #abstract class没法实例化, 就像自然界没有"动物"这么一种动物, 必须要生成"狗","猫"之类的才可以实例化
  #如果你尝试x = Animal(), 这是会报错的
  
  #为什么要有这么个class? 这就是规定了Animal统一的class标准, 而且继承Animal的class都要implement一个talk函数才能编译通过,
  #在软件工程里就是规定继承Base class的子类必须要implement它提到的纯虚函数
  @abstractmethod
  def talk(self): # Abstract method, defined by convention only
    pass

  def myname(self):
    return "my name is "+self.name

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
```
# 如何体现多态(polymorphism)?
就是你有一个list, 你知道它存着不同类型的derived class obj, 比如有猫有狗, 但是只有在run time, 你才知道这个obj是猫还是狗
然后在run time的时候, 你call这个obj的abstract method(talk)的时候, 它能出现基于derived class定义的不同的行为, 这就是多态的表现

```py
for animal in animals:
  print(animal.myname() + ': ' + animal.talk())
```

Polymorphism is the ability of an object to take on many forms. The most common use of polymorphism in OOP occurs when a parent class reference is used to refer to a child class object.

## 面试问题: "什么是polymorphism?" 回答3大关键点
1. Base type pointer (or reference)
2. Virtual method
3. Runtime

## CPP example

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Animal {
	protected:
	int m_id;
	
	public:
	Animal(int id): m_id(id){}
	//############# 3. Virtual ##############
	virtual void talk(){
		cout<<"id "<<m_id<<": animal talk"<<endl;
	}
	// 如果是纯虚函数的话，应该写成：
	virtual void talk()=0;
	// 如果返回值是int的话，就写int
	
};

class Cat : public Animal {
	public:
	Cat(int id):Animal(id){}
	virtual void talk(){
		cout<<"id "<<m_id<<": Cat talk"<<endl;
	}
};

class Dog : public Animal {
	public:
	Dog(int id):Animal(id){}
	virtual void talk(){
		cout<<"id "<<m_id<<": Dog talk"<<endl;
	}
};

int main(){
    //############# 1. Base type pointer ################## 
	vector<Animal*> animal_list;
	
	//################ 2. Run time ################
	while(true){
		string animal_name;
		cout << "Join an animal:";
		cin >> animal_name;
		
		if(animal_name == "Cat"){
			int id = animal_list.size();
			Animal * animal_ptr = new Cat(id);
			animal_list.push_back(animal_ptr);
		} else 
		if(animal_name == "Dog") {
			int id = animal_list.size();
			Animal * animal_ptr = new Dog(id);
			animal_list.push_back(animal_ptr);
		}
		
		for(int i=0; i<animal_list.size(); ++i){
			animal_list[i]->talk();
		}
	}
}
```
# 一个简易版本
```cpp
#include <iostream>
#include <string>

using namespace std;

class Animal{
    public:
        virtual void talk()=0;
};

class Dog: public Animal{ //publicly inherit Animal
    public:
        virtual void talk(){
            cout << "Wolf" << endl;
        }
};

class Cat: public Animal{
    public:
        virtual void talk(){
            cout << "Meow" << endl;
        }
};

int main(){
    Dog dog1; //C++中初始化函数没有写的话，实例化的时候就不需要带括号
    Cat cat1;
    Animal * prt = &dog1;
    prt->talk();
    prt = &cat1;
    prt->talk();
}
```
# Python版polymorphism (面试题)
```py
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, is_mammal, is_carnivorous):
        self.__is_mammal = is_mammal # 注意这里是private的
        self.__is_carnivorous = is_carnivorous
    
    def getISMammal(self):
        return self.__is_mammal
        
    def getIsCarnivorous(self):
        return self.__is_carnivorous 
    
    @abstractmethod
    def getGreeting(self):
        pass
    
    def printAnimal(self):
        print('A ',self.name, 'says ', self.getGreeting(), ',')
        print('is', '' if self.getISMammal() else ' not', ' a mammal,')
        print('is', '' if self.getIsCarnivorous() else ' not', ' carnivorous.')


class Dog(Animal):
    def __init__(self, name):
        super().__init__(True, True)
        self.name = name
        
    def getGreeting(self):
        return 'ruff'

class Cow(Animal):
    def __init__(self, name):
        super().__init__(True, False)
        self.name = name
    
    def getGreeting(self):
        return 'moo'
        
class Duck(Animal):
    def __init__(self, name):
        super().__init__(False, False)
        self.name = name
    
    def getGreeting(self):
        return 'quack'
    

if __name__ == '__main__':
    obj1 = Dog('dog')
    obj2 = Cow ('cow')
    obj3 = Duck('duck')
    for i in [obj1,obj2,obj3]:
        i.printAnimal()

```
## 结果
```py
A  dog says  ruff ,
is   a mammal,
is   carnivorous.
A  cow says  moo ,
is   a mammal,
is  not  carnivorous.
A  duck says  quack ,
is  not  a mammal,
is  not  carnivorous.
```

# BNP inheritance 原题
```cpp
#include <iostream>

using namespace std;

class Animal{
    
    protected:
    bool isMammal;
    bool isCarnivorous;
    
    public:
    Animal(bool isMammal, bool isCarnivorous){
        this->isMammal = isMammal;  //这里的this不能少，否则complier无法识别，结果就会不一样
        this->isCarnivorous = isCarnivorous;
    }
    bool getISMammal(){
        return this->isMammal;
    }
    bool getIsCarnivorous(){
        return this->isCarnivorous;
    }
    virtual string getGreeting()=0;
    void printAnimal(string name){
        cout << "A " << name << " says '" << this->getGreeting() << "', is"
        << (this->getIsCarnivorous() ? "" : " not") << " carnivorous, and is"
        << (this->getISMammal() ? "" : " not") << " a mammal." << endl;
    }
};

class Dog: public Animal{
    public:
    Dog(): Animal(true,true) {}
    
    virtual string getGreeting(){
        return "ruff";
    }
    
};

class Cow: public Animal{
    public:
    Cow(): Animal(true,false) {}
    virtual string getGreeting(){
        return "moo";
    }
};

class Duck: public Animal{
    public:
    Duck(): Animal(false,false) {}
    virtual string getGreeting(){
      return "quack";
        
    }
};

int main()
{
    Animal *pointer = new Dog;
    pointer->printAnimal("dog");
    pointer = new Duck;
    pointer->printAnimal("duck");
    pointer = new Cow;
    pointer->printAnimal("cow");
}


```

# Result
```cpp
A dog says 'ruff', is carnivorous, and is a mammal.                                                                     
A duck says 'quack', is not carnivorous, and is not a mammal.                                                           
A cow says 'moo', is not carnivorous, and is a mammal. 
```
# 知识点总结
1. C++的class如果没有声明，则默认所有的member variables 和 member functions 都是private的  
2. this的作用类似python中的self. 但不完全一样，但加this是有必要的  

# 不加this的result
```cpp
A dog says 'ruff', is not carnivorous, and is not a mammal.                                                             
A duck says 'quack', is not carnivorous, and is not a mammal.                                                           
A cow says 'moo', is not carnivorous, and is not a mammal. 
```
