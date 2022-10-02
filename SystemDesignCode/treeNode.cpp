#include <bits/stdc++.h>
using namespace std;
// tree node
struct Node {
    int data;
    Node *left, *right;
};

// returns a new tree Node
Node* newNode(int data) {
    Node* temp = new Node();
    temp->data = data;
    temp->left = temp->right = NULL;
    return temp;
}

// A function to create binary tree.
Node* Tree(Node* temp, int data) {
    // If the tree is empty, return a new node
    if (temp == NULL)
        return newNode(data);

    // Otherwise, recur down the tree
    if (data < temp->data)
        temp->left = Tree(temp->left, data);
    else
        temp->right = Tree(temp->right, data);

    //return the (unchanged) node pointer
    return temp;
}

//function to display all the element present in the binary tree
void display(struct Node* root) {

    if (!root)
    return;
        display(root->left);
        cout<<root->data<<" ";
        display(root->right);
}

//function to insert element in binary tree
void insert(struct Node* root , int value) {
    queue<struct Node*> q;
    q.push(root);

    // Do level order traversal until we find an empty place.
    while (!q.empty()) {
        struct Node* root = q.front();
        q.pop();

        if (!root->left) {
            root->left = newNode(value);
            break;
        } else
            q.push(root->left);

        if (!root->right) {
            root->right = newNode(value);
            break;
        } else
            q.push(root->right);
    }
}

int main() {
    char ch;
    int n;
    int arr[10] = {1,2,3,4,5,6,7};
    int size = 10;
    Node *root = new Node;
    root = NULL;
    // Construct the binary tree.
    /*for(int i = 0; i < size; i++)
    {
        root = Tree(root, arr[i]);
    }*/
    root = Tree(root, 5);
    insert(root,10);
    insert(root, 20);
    insert(root,30);
    insert(root, 40);
    insert(root, arr[2]);
    insert(root, arr[3]);
    
    cout<<"Elements are: ";
    display(root);
    cout<<endl;
    return 0;
}