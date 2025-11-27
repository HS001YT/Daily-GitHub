#include<bits/stdc++.h>
using namespace std;

class Solution {
  public:
    int countZeroes(vector<int> &arr) {
        int n = arr.size();
        int low = 0, high = n - 1;
        int firstZero = -1;

        while (low <= high) {
            int mid = low + (high - low) / 2;

            if (arr[mid] == 0) {
                firstZero = mid;     // potential first zero
                high = mid - 1;      // search left
            } else {
                low = mid + 1;       // move right
            }
        }

        if (firstZero == -1) return 0;  // no zeros in array

        return n - firstZero;           // count of zeros
    }
};
