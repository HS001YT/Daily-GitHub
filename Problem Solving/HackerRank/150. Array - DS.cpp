#include <bits/stdc++.h>
using namespace std;

vector<int> reverseArray(vector<int> v) {
    vector<int> a;
    for(auto it = v.rbegin(); it != v.rend(); it++) {
        a.push_back(*it);
    }
    return a;
}