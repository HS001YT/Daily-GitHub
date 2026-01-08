#include <iostream>
#include <cmath>
#include <cstdio>
using namespace std;

struct Node {
    int data;
    Node* left;
    Node* right;

    Node(int val) {
        data = val;
        left = right = NULL;
    }
};

// Insert into BST
Node* insert(Node* root, int data) {
    if (root == NULL)
        return new Node(data);

    if (data <= root->data)
        root->left = insert(root->left, data);
    else
        root->right = insert(root->right, data);

    return root;
}

// Preorder Traversal
void preOrder(Node* root) {
    if (root == NULL)
        return;

    cout << root->data << " ";
    preOrder(root->left);
    preOrder(root->right);
}

int main() {
    int n;
    cin >> n;

    Node* root = NULL;

    for (int i = 0; i < n; i++) {
        int data;
        cin >> data;
        root = insert(root, data);
    }

    preOrder(root);
    return 0;
}