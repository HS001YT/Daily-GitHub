#include <bits/stdc++.h>
using namespace std;

int pickingNumbers(vector<int> a) {
    vector<int> freq(101, 0); // since numbers are 0 <= a[i] <= 100
    
    // Count frequency of each number
    for(int num : a) {
        freq[num]++;
    }
    
    int max_len = 0;
    
    // Check subarrays with difference <= 1
    for(int i = 1; i <= 100; i++) {
        max_len = max(max_len, freq[i] + freq[i-1]);
    }
    
    return max_len;
}