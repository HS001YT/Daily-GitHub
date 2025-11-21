#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    int maxSubarraySum(vector<int> &arr) {
        int current = arr[0];
        int best = arr[0];

        for (int i = 1; i < arr.size(); i++) {
            current = max(arr[i], current + arr[i]);
            best = max(best, current);
        }

        return best;
    }
};
