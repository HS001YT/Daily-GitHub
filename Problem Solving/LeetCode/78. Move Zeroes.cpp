#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int last = 0; // index for the last non-zero found

        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != 0) {
                swap(nums[last], nums[i]);
                last++;
            }
        }
    }
};
