# Full example
```cpp
#include <iostream>
#include <cmath>

using namespace std;

class BinaryTree {
private: // member variables 最好都是private的；如果都是public则可直接用struct
    int val; 
    BinaryTree* left;
    BinaryTree* right;
public:
    BinaryTree(int v);
    ~BinaryTree(); // destructor
    void insert(int); // 可以只写parameter的type，不写input name
    void inorderTraverse();
    void preorderTraverse();
    void postorderTraverse();
    int height(BinaryTree*); // 可以只写parameter的type，不写input name
    int max();
    int min();
    bool find(int v); // binary search
    BinaryTree* removeNode(BinaryTree* root, int v); // 删除节点，这里如果是传root的pointer，则必须要返回prt
    // void removeNode(BinaryTree** root, int v); // 如果不返回，则必须用double pointer
    BinaryTree* findMin(BinaryTree* node); // 任意给一个nodeprt，得到该节点之下的最小值的nodeprt，用于remove
    BinaryTree* findMin2(BinaryTree* node); //iteration version
    void deleteTree(BinaryTree* root); // remove 整个tree
    
};

BinaryTree::BinaryTree(int v){
    val = v;
    left = right = NULL; //赋值可以连写
}

BinaryTree::~BinaryTree() {} //这种简写形式不需要加；

void BinaryTree::deleteTree(BinaryTree* root){ // postorderTraverse 适用于 delete the whole tree
    if(root){
        deleteTree(root->left);
        deleteTree(root->right);
        delete root;
        root = NULL;
    }
}

void BinaryTree::insert(int v){
    if(v<val){
        if(left)
            left->insert(v);
        else
            left = new BinaryTree(v);
    }
    else{
        if(right)
            right->insert(v);
        else
            right = new BinaryTree(v);
    }
}

bool BinaryTree::find(int v){
    if(val==v)
        return true;
    else{
        if(v<val){
            if(left)
                left->find(v);
            else
                return false;
        }
        else{
            if(right)
                right->find(v);
            else
                return false;
        }
    }
}

int BinaryTree::max(){
    if(!right)
        return val;
    return right->max();
}

int BinaryTree::min(){
    if(!left)
        return val;
    return left->min();
}

int BinaryTree::height(BinaryTree* root){ // root必须要作为参数传入
    if(!root)
        return 0;
    return std::max(1+height(root->left), 1+height(root->right)); //不能单独写left，虽然是member function，但只是为了能调用private variable
}

void BinaryTree::preorderTraverse(){
    cout << val << " ";
    if(left) // 任何需要用left或right来call其他function的argument之前，都要先检验left是否为空
        left->preorderTraverse();
    if(right)
        right->preorderTraverse();
}

void BinaryTree::inorderTraverse(){
    if(left)
        left->inorderTraverse();
    cout << val << " ";
    if(right)
        right->inorderTraverse();
}

void BinaryTree::postorderTraverse(){
    if(left)
        left->postorderTraverse();
    if(right)
        right->postorderTraverse();
    cout << val << " ";
}

BinaryTree* BinaryTree::findMin(BinaryTree* node_prt){ //recursion
    if(node_prt->left){
        findMin(node_prt->left);
    }
    else{
        return node_prt;
    }
}

BinaryTree* BinaryTree::findMin2(BinaryTree* node_prt){ // iteration
    while(node_prt->left)
        node_prt = node_prt->left;
    return node_prt;
}

BinaryTree* BinaryTree::removeNode(BinaryTree* root, int v){ // removeNode的逻辑和find类似，因为要先找到那个节点才能删除
    if(!root) return root; //如果root为空，说明没有找到val=v的节点
    else if(v<root->val) root->left = removeNode(root->left, v); // 在left tree里search，同时因为left tree之后会被改变，所以return新的left tree节点
    else if(v>root->val) root->right = removeNode(root->right, v); //注意这里的写法和在main里call这个function是完全一致的，旧的prt作为传参，新的prt会被返回
    else{ // val==v，以下为找到节点之后的三种情况
        if(!root->left && root->right){ // case 1 （1）： 只有right child （直接用child来顶替，类似linked list）
            BinaryTree* temp = root; // 先copy要删除的节点
            root = root->right; // 把root prt和right child连上
            delete temp; // 删除不要的节点
        }
        else if(!root->right && root->left){ // case 1 （2）: 只有left child
            BinaryTree* temp = root;
            root = root->left;
            delete temp;
        }
        else if(!root->right && !root->left){ // case 2: 此节点为根节点（leaf） 
            delete root; // 释放root指向的heap上的那块内存，root这个prt还存在在stack上
            root = NULL; // 让root prt指向null
        }
        else{ // case 3: 有left child 和right child
            BinaryTree* temp = findMin2(root->right);
            root->val = temp->val;
            root->right = removeNode(root->right, temp->val);
        }
    }
    return root;
}


int main(){
    BinaryTree* head = new BinaryTree(8);
    int array[] = {4,2,6,1,3,5,7,12,10,9,11};
    for(int number:array){
        head->insert(number);
    }
    head->inorderTraverse();
    cout << endl;
    cout << (head->find(8)? "yes":"no") << endl;
    cout << (head->find(12)? "yes":"no") << endl;
    head->preorderTraverse();
    cout << endl;
    cout <<"min is: " << head->min() << endl;
    cout << "max is: " << head->max() << endl;
    cout << "height is: " << head->height(head) << endl;
    head->postorderTraverse();
    head->insert(15);
    head->insert(17);
    head->insert(16);
    head = head->removeNode(head, 15);
    // head->removeNode(head, 5);
    cout << endl;
    head->inorderTraverse();
    // head = head->removeNode(head, 3);
    cout << endl;
    head->deleteTree(head);
    cout << ((head==NULL)? "yes":"no") << endl;
    
}


```

# Result
```cpp
1 2 3 4 5 6 7 8 9 10 11 12                                                                                              
yes                                                                                                                     
yes                                                                                                                     
8 4 2 1 3 6 5 7 12 10 9 11                                                                                              
min is: 1                                                                                                               
max is: 12                                                                                                              
height is: 4                                                                                                            
1 3 2 5 7 6 4 9 11 10 12 8                                                                                              
1 2 3 4 5 6 7 8 9 10 11 12 16 17                                                                                        
no                                                                                                                      
    
```
