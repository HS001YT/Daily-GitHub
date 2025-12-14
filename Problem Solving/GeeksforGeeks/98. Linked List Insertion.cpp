#include <bits/stdc++.h>
using namespace std;

class Node {
  public:
    int data;
    Node *next;

    Node(int x) {
        data = x;
        next = NULL;
    }
};

class Solution{
public:
    // Function to insert a node at the beginning of the linked list.
    Node* insertAtFront(Node *head, int x) {
        Node* newNode = new Node(x);   // create new node
        newNode->next = head;          // link new node to old head
        return newNode;                // new node becomes the new head
    }
};

