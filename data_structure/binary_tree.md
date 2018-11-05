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
    int value;
    Node * left;
    Node * right;
    
    Node(int v){
        value = v;
        left = right = NULL;
    }
};

void insertNode(Node * node, int data){
    if(data<=node->value){
        if(node->left==NULL){
            node->left = new Node(data);
        }
        else{
            insertNode(node->left, data);
        }
    }
    if(data>node->value){
        if(node->right==NULL){
            node->right = new Node(data);
        }
        else{
            insertNode(node->right, data);
        }
    }
};

void traversal_inorder(Node * node){
    if(!node){
        return;
    }
    traversal_inorder(node->left);
    cout<<node->value<<" ";
    traversal_inorder(node->right);
};

void traversal_preorder(Node * node){
    if(!node){
        return;
    }
    cout<<node->value<<" ";
    traversal_preorder(node->left);
    traversal_preorder(node->right);
};

void traversal_postorder(Node * node){
    if(!node){
        return;
    }
    traversal_postorder(node->left);
    traversal_postorder(node->right);
    cout<<node->value<<" ";
};

int main()
{
    Node * root = new Node(10);
    root->left = new Node(8);
    root->right = new Node(12);
    insertNode(root, 4);
    insertNode(root, 3);
    insertNode(root, 15);
    insertNode(root, 5);
    insertNode(root, 9);
    insertNode(root, 11);
    
    traversal_postorder(root);
    cout<<endl;
    traversal_preorder(root);
    cout<<endl;
    traversal_inorder(root);
    
}


```
# Output
```cpp
3 5 4 9 8 11 15 12 10                                                                                                   
10 8 4 3 5 9 12 11 15                                                                                                   
3 4 5 8 9 10 11 12 15 
```
