# what's included:
1. namespace 正确用法  
2. template class 用法  
3. const getter 用法和写法  
4. pointer to pointer 传参写法  
5. insert的recursion和iteration写法  
6. template 在heap上初始化写法

# Code
```cpp
#include <iostream>
#include <string>

using std::cout;
using std::endl;
using std::string;
using std::swap;

template<typename T> // class 之前必须写上这个，只有T是可以自己改的，其他格式都是固定的
class LinkedList {
    T val; // member variable 尽量都应该写成private
    LinkedList* next; // 因为任何需要的改动都应该由class的member functions来完成
public:
    LinkedList(T v): val(v), next(NULL) {} // 初始化func的简写形式，没有“；”
    void append(T v);
    void print();
    void insert(T v, int position);
    void prepend(T v, LinkedList** head); // double pointer 的传参写法
    void deleteNode(T v, LinkedList** head);
    int size();
    LinkedList* getNext() const; // const member function的写法
    T getVal() const;
};

template<typename T> //每一个member function在class外部定义的时候都应该加上template定义
void LinkedList<T>::print(){ // 包括class name本身也要加上template typename，表示这是一个template class
    cout << val << " ";
    if(next)
     return next->print();
}

template<typename T>
void LinkedList<T>::append(T v){
    if(!next){
        next = new LinkedList(v);
        return;
    }
    return next->append(v);
}

template<typename T>
void LinkedList<T>::prepend(T v, LinkedList** head){
    LinkedList* new_node = new LinkedList(v);
    new_node->next = *head; // double pointer作为参数的用法，都是只能少一个*
    *head = new_node; // 表示取double pointer指向内存的content，并对它进行修改
}

template<typename T>
void LinkedList<T>::insert(T v, int position){
    /// 以下为recursive 写法
    // if(position==1){
    //     LinkedList* new_node = new LinkedList(v);
    //     new_node->next = next;
    //     next = new_node;
    //     return;
    // }
    // return next->insert(v, position-1);
    LinkedList* temp = this;
    for(int i=0; i<position-1; i++){
        temp = temp->next;
    }
    LinkedList* new_node = new LinkedList(v);
    new_node->next = temp->next;
    temp->next = new_node;
}

template<typename T>
void LinkedList<T>::deleteNode(T v, LinkedList** head){
    if(val==v){
        LinkedList* temp = *head;
        *head = next;
        delete(temp); // 一定要记住删除掉的node要进行memory deallocation
        return;
    }
    if(!next){ //一定要注意遇到if后面跟的是next->val 的情况，应该首先要检测next是否为NULL
        cout << "value not found" << endl;
        return;
    }
    else if(next->val==v){ 
        LinkedList* temp = next;
        next = next->next;
        delete(temp);
        return;
    }
    else{
        return next->deleteNode(v, head); //这里再传入的double pointer不用加*，因为本身主func就传的是head
    }
    
}

template<typename T>
int LinkedList<T>::size(){
    if(!next){
        return 1; // 注意这里是1，不是0
    }
    return 1 + next->size();
}

template<typename T>
LinkedList<T>* LinkedList<T>::getNext() const{
    return next;
}

template<typename T>
T LinkedList<T>::getVal() const{
    return val;
}

int main() {
    LinkedList<int>* head = new LinkedList<int>(0); //注意new template class 的写法，包括前面的pointer类型也要加typename
    head->append(1);
    head->append(2);
    head->append(3);
    head->print();
    cout << endl;
    head->prepend(10, &head);
    head->print();
    cout << endl;
    head->insert(8, 3);
    head->print();
    cout << endl;
    head->insert(6, 0);
    head->print();
    cout << endl;
    head->deleteNode(8, &head);
    head->print();
    cout << endl;
    head->deleteNode(10, &head);
    head->print();
    cout << endl;
    head->deleteNode(10, &head);
    
    LinkedList<char>* l = new LinkedList<char>('a'); // 体现了support multiple data type
    l->append('b');
    l->append('c');
    l->print();
    cout << endl;
    l->prepend('y', &l);
    l->print();
    cout << endl;
    l->insert('t', 2);
    l->print();
    cout << endl;
    l->deleteNode('b', &l);
    l->print();
    cout << endl;
    l->deleteNode('z', &l);
    
}
```
