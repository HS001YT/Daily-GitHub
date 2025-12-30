#include <iostream> 
#include <cstdio> 
#include <cmath> 
#include <vector> 
#include <unordered_map> 
using namespace std;

class Node {
public:
    int key, value;
    Node* prev;
    Node* next;

    Node(int k, int v) {
        key = k;
        value = v;
        prev = next = NULL;
    }
};

class LRUCache {
    int cp;
    unordered_map<int, Node*> mp;
    Node* head;
    Node* tail;

public:
    LRUCache(int capacity) {
        cp = capacity;
        head = tail = NULL;
    }

    int get(int key) {
        if (mp.find(key) == mp.end())
            return -1;

        Node* node = mp[key];
        moveToHead(node);
        return node->value;
    }

    void set(int key, int value) {
        if (mp.find(key) != mp.end()) {
            Node* node = mp[key];
            node->value = value;
            moveToHead(node);
            return;
        }

        if (mp.size() == cp) {
            mp.erase(tail->key);
            Node* prev = tail->prev;
            delete tail;
            tail = prev;
            if (tail) tail->next = NULL;
            else head = NULL;
        }

        Node* node = new Node(key, value);
        node->next = head;
        if (head) head->prev = node;
        head = node;
        if (!tail) tail = head;

        mp[key] = node;
    }

private:
    void moveToHead(Node* node) {
        if (node == head) return;

        if (node->prev) node->prev->next = node->next;
        if (node->next) node->next->prev = node->prev;
        if (node == tail) tail = node->prev;

        node->prev = NULL;
        node->next = head;
        if (head) head->prev = node;
        head = node;
    }
};

int main() {
    int n, capacity;
    cin >> n >> capacity;

    LRUCache cache(capacity);

    while (n--) {
        string cmd;
        cin >> cmd;
        if (cmd == "set") {
            int key, value;
            cin >> key >> value;
            cache.set(key, value);
        } else {
            int key;
            cin >> key;
            cout << cache.get(key) << endl;
        }
    }
    return 0;
}
