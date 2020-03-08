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

template<typename T>
class LinkedList {
    T val;
    LinkedList* next;
public:
    LinkedList(T v): val(v), next(NULL) {}
    void append(T v);
    void print();
    void insert(T v, int position);
    void prepend(T v, LinkedList** head);
    void deleteNode(T v, LinkedList** head);
    int size();
    LinkedList* getNext() const;
    T getVal() const;
};

template<typename T>
void LinkedList<T>::print(){
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
    new_node->next = *head;
    *head = new_node;
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
        delete(temp);
        return;
    }
    if(!next){
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
        return next->deleteNode(v, head);
    }
    
}

template<typename T>
int LinkedList<T>::size(){
    if(!next){
        return 1;
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
    LinkedList<int>* head = new LinkedList<int>(0);
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
    
    LinkedList<char>* l = new LinkedList<char>('a');
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
