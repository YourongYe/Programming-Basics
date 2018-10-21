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
