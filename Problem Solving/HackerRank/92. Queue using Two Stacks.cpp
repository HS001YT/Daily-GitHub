#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <stack>
using namespace std;


int main() {
    stack<long> s1, s2;
    int q;
    cin >> q;

    while(q--) {
        int type;
        cin >> type;

        if(type == 1) {
            long x;
            cin >> x;
            s1.push(x);
        }
        else {
            if(s2.empty()) {
                while(!s1.empty()) {
                    s2.push(s1.top());
                    s1.pop();
                }
            }

            if(type == 2) {
                if(!s2.empty()) s2.pop();
            }
            else if(type == 3) {
                if(!s2.empty()) cout << s2.top() << "\n";
            }
        }
    }

    return 0;
}
