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
    Node * nodeprt = new Node();
    nodeprt->data = data;
    nodeprt->left = NULL;
    nodeprt->right = NULL;
    return nodeprt;
}

int main(){
    Node * root = newnode(9);
    root->left = newnode(4);
    root->right = newnode(10);
    root->left->left = newnode(1);
    root->left->right = newnode(5);
    cout << root->left->right->data;
}
```

# max depth of binary tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
```cpp
//https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if(!root){
            return 0;
        }
        
        return 1+std::max(maxDepth(root->left),maxDepth(root->right));
    }
};
```

# 创建二叉树和遍历
```cpp
/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>

using namespace std;

struct Node{
    int data;
    Node * left;
    Node * right;
    Node(int v){
        data = v;
        left = right = NULL;
    }
};

void insertNode(Node * node, int value){
    if(value<=node->data){
        if(node->left==NULL){
            node->left = new Node(value);
        }
        else{
            insertNode(node->left,value);
        }
    }
    if(value>node->data){
        if(node->right==NULL){
            node->right = new Node(value);
        }
        else{
            insertNode(node->right,value);
        }
    }
}

void preorder(Node * node){
    if(node){
    cout<<node->data<<" ";
    preorder(node->left);
    preorder(node->right);
    }
}

int main()
{
    Node * root = new Node(8);
    insertNode(root,7);
    cout<<root->data<<endl;
    for(int i=0; i<15; i++){
        insertNode(root,i);
    }
    
    preorder(root);
    
    
}

```
