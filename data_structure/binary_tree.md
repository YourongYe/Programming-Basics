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
    
    traversal_postorder(root); // left->right->root
    cout<<endl;
    traversal_preorder(root);  // root->left->right
    cout<<endl;
    traversal_inorder(root);  // left->root->right
    
}


```
# Output
```cpp
3 5 4 9 8 11 15 12 10                                                                                                   
10 8 4 3 5 9 12 11 15                                                                                                   
3 4 5 8 9 10 11 12 15 
```
# Full example
```cpp
#include <iostream>
using namespace std;

class BinTree{
	int val;
	BinTree *left;
	BinTree *right;
	
	public:
	BinTree(int);
	~BinTree();
	void insert(int);
	bool find(int);
	int min();
	int max();
	void walk();
	void erase(int);
};

BinTree::BinTree(int x){
	val = x;
	left = right = NULL;
}
BinTree::~BinTree(){}

void BinTree::insert(int x){
	if(x<val){
		if(left==NULL){
			left = new BinTree(x);
		}
		else{
			left->insert(x);
		}
	}
	if(x>val){
		if(right==NULL){
			right = new BinTree(x);
		}
		else{
			right->insert(x);
		}
	}

}

bool BinTree::find(int x){ 
	if(x==val){
		return true;
	}
	if(x>val){
	    if(right){
		    right->find(x);
	    }
	    else{
	        return false;
	    }
	}
	if(x<val){
	    if(left){
		    left->find(x);
	    }
	    else{
	        return false;
	    }
	}
}

int BinTree::min(){
    while(left->left!=NULL){
        left = left->left;
    }
    return left->val;
}

int BinTree::max(){
    while(right->right!=NULL){
        right = right->right;
    }
    return right->val;
}

void BinTree::walk(){
    if(left){
    left->walk();
    }
    cout<<val<<" ";
    if(right){
    right->walk();
    }
}

int main() {
    BinTree root(5);
    for(int i=0; i<=30; i++){
        if(i!=5){
        root.insert(i);
        }
    }
    
    root.walk();
    
    if(root.find(34)){
        cout<<"yes"<<endl;
    }
    else{
        cout<<"no"<<endl;
    }
    
    cout<<root.max()<<endl;
    cout<<root.min()<<endl;
}
```
# Result
```cpp
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30                                      
no                                                                                                                      
30                                                                                                                      
0  
```
