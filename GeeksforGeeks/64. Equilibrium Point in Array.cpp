#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    // Function to find equilibrium point in the array.
    int findEquilibrium(vector<int> &arr) {
        int n = arr.size();
        
        // If only one element, it's the equilibrium point
        if (n == 1) return 0;  // Note: 0-based index
        
        long long totalSum = 0, leftSum = 0;
        
        // Step 1: Find total sum of elements
        for (int i = 0; i < n; i++)
            totalSum += arr[i];
            
        // Step 2: Iterate and find equilibrium index
        for (int i = 0; i < n; i++) {
            totalSum -= arr[i]; // totalSum now represents right sum
            
            if (leftSum == totalSum)
                return i; // Return equilibrium index (0-based)
                
            leftSum += arr[i];
        }
        
        return -1; // No equilibrium index found
    }
};