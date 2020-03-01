# Uncommon implementation
```cpp

/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

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

# Common implementation
```
/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

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

```cpp
