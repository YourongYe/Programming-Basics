# Node class and LinkedList class
```cpp

#include <iostream>

using namespace std;

class Node {
public:
    int val;
    Node* next;
    Node(int v){
        this->val = v;
        this->next = NULL;
    }
};

class LinkedList {
private:
    Node* head;
public:
    LinkedList(){
        this->head = NULL;
    }
    void print();
    void append(int v);
    void insert(int v, int position);
    void deleteElement(int position);
};

void LinkedList::append(int v){
    Node* temp = this->head;
    if(temp==NULL){
        this->head = new Node(v);
    }
    else{
        while(temp->next!=NULL){
            temp = temp->next;
        }
        temp->next = new Node(v);
    }
    
}

void LinkedList::print(){
    Node* temp = this->head;
    while(temp){
        cout << temp->val << " ";
        temp = temp->next;
    }
    cout << endl;
}

void LinkedList::insert(int v, int position){
    Node* temp = this->head;
    if(position==0){
        this->head = new Node(v);
        this->head->next = temp;
    }
    else{
        for(int i=0; i<position-1; i++){
            temp = temp->next;
        }
        // Node* later_part = temp->next;
        Node* new_node = new Node(v);
        new_node->next = temp->next;
        temp->next = new_node;
    }
    
}

void LinkedList::deleteElement(int position){
    Node*temp = this->head;
    while(position>1){
        temp = temp->next;
        position--;
    }
    temp->next = temp->next->next;
    //should i delete the node?
}


int main()
{
    LinkedList* list_example = new LinkedList();
    list_example->append(2);
    list_example->append(3);
    list_example->append(4);
    list_example->print();
    list_example->insert(10, 2);
    list_example->print();
    list_example->insert(66, 0);
    list_example->print();
    list_example->deleteElement(2);
    list_example->print();
    list_example->deleteElement(3);
    list_example->print();
}

```
# Node class only (with head outside, iteration version)
```cpp
/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>

using namespace std;

class Node {
    int val;
    Node *next;
    int size;
    
public:
    Node(int v): val(v), next(NULL), size(1) {}
    void addToTail(int v);
    void addToHead(int v, Node **head);
    void insert(int v, int position);
    void deleteNode(int v, Node** head_ref);
    void print();
    void getSize();
};

void Node::addToTail(int v){
    Node *temp = this;
    while(temp->next){
        temp = temp->next;
    }
    temp->next = new Node(v);
    this->size++;
}

void Node::addToHead(int v, Node **head_ref){
    Node *new_node = new Node(v);
    new_node->next = *head_ref;
    *head_ref = new_node;
    this->size++;
    cout << "head_ref: " << head_ref << endl;
    cout << "*head_ref: " << *head_ref << endl;
    // cout << **head_ref << " ";
}

void Node::insert(int v, int position){
    Node *temp = this;
    Node *new_node = new Node(v);
    int i = position-1;
    while(i>0){
        temp = temp->next;
        i--;
    }
    new_node->next = temp->next;
    temp->next = new_node;
    this->size++;
}

void Node::print(){
    Node *temp = this;
    while(temp){
        cout << temp->val << " ";
        temp = temp->next;
    }
    cout << endl;
}

void Node::deleteNode(int v, Node** head_ref){ // 参数必须有head的double pointer，因为当删除的node是head时，需要改变head指向的address
    Node* temp = this;
    Node* prev;
    this->size--;
    if (temp->val == v){
        *head_ref = temp->next; // 对double pointer 的dereference，把第一个pointer存的address改掉
        free(temp); // deallocate memory
        return;
    }
    while(temp->val != v){ //如果要删除的不是第一个node
        prev = temp;
        temp = temp->next;
    }
    prev->next = temp->next;
    free(temp);
    return;
}

void Node::getSize(){
    cout << this->size << endl;
}

int main()
{
    Node *head = new Node(1);
    head->addToHead(0, &head);
    head->addToTail(2);
    head->addToTail(5);
    head->addToTail(8);
    head->print();
    head->addToTail(3);
    head->addToHead(-1, &head);
    head->print();
    head->insert(66, 2);
    head->print();
    head->deleteNode(66, &head);
    head->print();
    head->deleteNode(-1, &head);
    head->print();
    head->getSize();
    
}

```
# Results
```cpp
head_ref: 0x7ffd303ecc88                                                                                                
*head_ref: 0x24cac40                                                                                                    
0 1 2 5 8                                                                                                               
head_ref: 0x7ffd303ecc88                                                                                                
*head_ref: 0x24cace0                                                                                                    
-1 0 1 2 5 8 3                                                                                                          
-1 0 66 1 2 5 8 3                                                                                                       
-1 0 1 2 5 8 3                                                                                                          
0 1 2 5 8 3                                                                                                             
6  
```

# Node class only (recursive version)
```cpp

#include <iostream>

using std::cout;
using std::endl;

class LinkedList {
    int val;
    LinkedList* next;
    // int size;
    
public:
    LinkedList(int v): val(v), next(NULL) {}
    void print() const;
    void append(int n);
    void insert(int position, int num);
    void deleteNode(int n, LinkedList** head);
    int size() const;
    LinkedList* getNext() const;
    int getValue() const;
};

LinkedList* LinkedList::getNext() const{
    return next;    
}

int LinkedList::getValue() const{
    // val = 10; // error: assignment of member ‘LinkedList::val’ in read-only object
    return val;
}

void LinkedList::print() const{
    cout << val << " ";
    if(next){
        next->print();  
    }  
    else{
        cout << endl;
    }
}

void LinkedList::append(int n){
    if(not next){
        next = new LinkedList(n);
        // size++;
    }
    else{
        next->append(n);
    }
    
}

void LinkedList::insert(int position, int num){
    if(position!=1){
        next->insert(position-1, num);
    }
    else{
        LinkedList* new_node = new LinkedList(num);
        new_node->next = next;
        next = new_node;
    }
}

int LinkedList::size() const{
    if(next){
        return next->size() + 1;
    }
    else{
        return 1;
    }
}

void LinkedList::deleteNode(int n, LinkedList** head){
    if(val == n){
        LinkedList* node = *head;
        *head = next;
        delete node;
        return;
    }
    if(not next){
        cout << "value not found" << endl;
        return;
    }
    else if(next->val == n){
        LinkedList* node = next;
        next = next->next;
        delete node;
        return;
    }
    else{
        next->deleteNode(n, head);
    }
}

int main()
{
    LinkedList* head = new LinkedList(0);
    // append some values
    head->append(1);
    head->append(2);
    head->append(3);
    head->append(4);
    // print them out
    head->print();
    // get the size
    cout << head->size() << endl;
    // insert a value to a given position
    head->insert(2, 10);
    head->print();
    cout << head->size() << endl;
    // insert a value to the end
    head->insert(6, 60);
    head->print();
    cout << head->size() << endl;
    // get the next and value from outside of the class
    LinkedList* temp = head;
    while(temp){
        cout << temp->getValue() << " ";
        temp = temp->getNext();
    }
    cout << endl;
    // delete a node at a given position
    head->deleteNode(100, &head);
    head->print();
    
    const LinkedList* prt = new LinkedList(10);
    // prt->append(20); //  error: passing ‘const LinkedList’ as ‘this’ argument discards qualifiers [-fpermissive]
    //因为这里next（member variable）会试图被改变
    
    
}

```
# Result
```cpp
0 1 2 3 4                                                                                                               
5                                                                                                                       
0 1 10 2 3 4                                                                                                            
6                                                                                                                       
0 1 10 2 3 4 60                                                                                                         
7                                                                                                                       
0 1 10 2 3 4 60                                                                                                         
value not found                                                                                                         
0 1 10 2 3 4 60    
```

# Uncommon implementation
```cpp

#include <iostream>

using namespace std;

class Node{
    public:
    int value;
    Node * next;
    Node(int v){
        value = v;
    }
};

class List{
    private:
    Node * m_head;
    
    public:
    List(int n){
        if(n<=0){
            cout<<"invalid n"<<endl;
            return;
        }
        
        cout<<"init "<<n<<" elements"<<endl;
        m_head = new Node(0);
        Node * node_iter = m_head;
        for(int i=1;i<n;++i){
            Node * node_ptr = new Node(i);
            node_iter->next = node_ptr;
            node_iter = node_iter->next;
        }
    }
    
    void printAllElem(){
        Node * iter = m_head;
        while(iter){
            cout<<iter->value<<endl;
            iter=iter->next;
        }    
    }
    
    void delElem(int i){
        Node * iter = m_head;
        if(i==m_head->value){
            m_head = m_head->next;
        }
        else{
            while(iter){
                if(iter->next->value==i){
                    iter->next = iter->next->next;
                    break;
                }
                iter = iter->next;
                
            }
        }
    }
};

int main(){
    List l = List(7);
    l.printAllElem();
    l.delElem(0);
    l.printAllElem();
}


```
