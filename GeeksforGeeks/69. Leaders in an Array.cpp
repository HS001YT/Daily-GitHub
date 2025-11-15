#include<bits/stdc++.h>
using namespace std;

class Solution {
    // Function to find the leaders in the array.
  public:
    vector<int> leaders(vector<int>& arr) {
        
        int n = arr.size();
        vector<int> result;
        
        int maxRight = arr[n - 1];
        result.push_back(maxRight);
        
        // Traverse from right to left
        for (int i = n - 2; i >= 0; i--) {
            if (arr[i] >= maxRight) {
                maxRight = arr[i];
                result.push_back(maxRight);
            }
        }
        
        // Leaders collected from right to left, so reverse
        reverse(result.begin(), result.end());
        return result;
        
    }
};