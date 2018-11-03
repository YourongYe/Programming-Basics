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
