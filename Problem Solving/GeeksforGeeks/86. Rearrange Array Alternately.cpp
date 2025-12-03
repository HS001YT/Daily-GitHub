#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    void rearrange(vector<int>& arr) {
        int n = arr.size();
        if (n <= 1) return;

        // Make a sorted copy
        vector<int> s = arr;
        sort(s.begin(), s.end());

        int l = 0, r = n - 1;
        vector<int> res(n);

        for (int i = 0; i < n; ++i) {
            if ((i & 1) == 0) {
                res[i] = s[r--]; // place next maximum
            } else {
                res[i] = s[l++]; // place next minimum
            }
        }

        // copy back
        for (int i = 0; i < n; ++i) arr[i] = res[i];
    }
};