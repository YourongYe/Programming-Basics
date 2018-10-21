# Basics
root：最顶部
  leaf：最底部
  depth(height):离root最远的Leaf的层


# C++ implementation
```cpp

#include <iostream>

using namespace std;

struct Node{
    int data;
    Node * left;
    Node * right;
};

Node * newnode(int data){
    Node * newnode = new Node();
    newnode->data = data;
    newnode->left = NULL;
    newnode->right = NULL;
    return newnode;
}



int main()
{
    Node * root = newnode(9);
    root->left = newnode(8);
    root->right = newnode(10);
    root->right->right = newnode(45);
    cout << root->right->right->data;
    return 0;
}




```
