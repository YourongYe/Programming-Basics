```cpp
#include <iostream>
#include <string>

using namespace std;

int add(int a, int b){
    return a+b;
}

int add(int a, int b, int c){
    return a+b+c;
}

std::string add(std::string a, std::string b, std::string c){
    return a+"+"+b+"+"+c;
}

int main()
{
    cout<<add(1,2)<<endl;
    cout<<add(1,2,3)<<endl;
    cout<<add("a","b","blabla")<<endl;

    return 0;
}
```

```python
#overload?
def add(a,b):
    return a+b

#第二个函数会覆盖掉第一个, 导致add(1,2)跑不出来
def add(a,b,c):
    return a+b+c
    
print(add(1,2))
```

```python
#如果想让add同时支持2个和3个input
def add(a,b,c=0):
    return a+b+c
    
print(add(1,2))
```
