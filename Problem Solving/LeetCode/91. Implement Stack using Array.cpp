#include <bits/stdc++.h>
#include<queue>
using namespace std;

class MyStack {
public:
    queue<int> q;

    MyStack() {
    }
    
    void push(int x) {
        q.push(x);
        int size = q.size();
        // Rotate the queue to make the last pushed element appear in front
        while (size > 1) {
            q.push(q.front());
            q.pop();
            size--;
        }
    }
    
    int pop() {
        int topVal = q.front();
        q.pop();
        return topVal;
    }
    
    int top() {
        return q.front();
    }
    
    bool empty() {
        return q.empty();
    }
};
