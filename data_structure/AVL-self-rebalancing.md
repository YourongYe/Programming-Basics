# Example
https://www.geeksforgeeks.org/avl-tree-set-1-insertion/
```cpp
#include <iostream>
#include <cmath>

using std::cout;
using std::endl;
using std::max;

class BinaryTree {
    int value;
    BinaryTree* left;
    BinaryTree* right;
    int height;

public:
    BinaryTree(int v);
    ~BinaryTree() {}
    BinaryTree* insert(BinaryTree* root, int v);
    int getHeight(BinaryTree* node);
    int getBalance(BinaryTree* node);
    BinaryTree* leftRotate(BinaryTree* node);
    BinaryTree* rightRotate(BinaryTree* node);
    void preorderTraverse();
    
};

BinaryTree::BinaryTree(int v){
    value = v;
    left = right = NULL;
    height = 1;
}

void BinaryTree::preorderTraverse(){
    cout << value << " ";
    if(left) left->preorderTraverse();
    if(right) right->preorderTraverse();
}

int BinaryTree::getHeight(BinaryTree* node){
    if(!node)
        return 0;
    return node->height;
}

int BinaryTree::getBalance(BinaryTree* node){
    if(node)
        return getHeight(node->left) - getHeight(node->right);
}

BinaryTree* BinaryTree::leftRotate(BinaryTree* node){
    BinaryTree* oldHead = node;
    BinaryTree* newHead = node->right;
    
    oldHead->right = newHead->left;
    newHead->left = oldHead;
    
    //update height
    oldHead->height = 1 + max(getHeight(oldHead->left), getHeight(oldHead->right));
    newHead->height = 1 + max(getHeight(newHead->left), getHeight(newHead->right));
    
    return newHead;
}

BinaryTree* BinaryTree::rightRotate(BinaryTree* node){
    BinaryTree* oldHead = node;
    BinaryTree* newHead = node->left;
    
    oldHead->left = newHead->right;
    newHead->right = oldHead;
    
    //update height
    oldHead->height = 1 + max(getHeight(oldHead->left), getHeight(oldHead->right));
    newHead->height = 1 + max(getHeight(newHead->left), getHeight(newHead->right));
    
    return newHead;
}

BinaryTree* BinaryTree::insert(BinaryTree* root, int v){
    if(!root){
        BinaryTree* newNode = new BinaryTree(v);
        return newNode;
    }
    else if(v<root->value) root->left = insert(root->left, v);
    else if(v>root->value) root->right = insert(root->right, v);
    else return root;
    //update height
    root->height = 1 + max(getHeight(root->left), getHeight(root->right));
    //get balance
    int balance = getBalance(root);
    // cout << "balance of" << root->value << "is" << balance << endl;
    //left left case
    if(balance>1 && v<root->left->value){
        // cout << "case1" << endl;
        return rightRotate(root);
    }
    //left right case
    if(balance>1 && v>root->left->value){
        // cout << "case2" << endl;
        root->left = leftRotate(root->left);
        return rightRotate(root);
    }
    //right right case
    if(balance<-1 && v>root->right->value){
        // cout << "case3" << endl;
        return leftRotate(root);
    }
    //right left case
    if(balance<-1 && v<root->right->value){
        // cout << "case4" << endl;
        root->right = rightRotate(root->right);
        return leftRotate(root);
    }
    return root;
}

int main(){
    BinaryTree* root = new BinaryTree(3);
    root = root->insert(root, 5);
    root = root->insert(root, 6);
    root = root->insert(root, 8);
    root = root->insert(root, 7);
    root->preorderTraverse(); //preorder can check the bst shape
}

```

# Result
```cpp
5 3 7 6 8
```
