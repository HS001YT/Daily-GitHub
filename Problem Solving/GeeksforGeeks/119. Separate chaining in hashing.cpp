#include <vector>
using namespace std;

class Solution {
  public:
    vector<vector<int>> separateChaining(int hashSize, vector<int>& arr) {
        // Step 1: Initialize hash table with empty vectors
        vector<vector<int>> hashTable(hashSize);

        // Step 2: Insert elements into hash table
        for (int num : arr) {
            int index = num % hashSize;  // hash function
            hashTable[index].push_back(num);  // append to the chain
        }

        return hashTable;
    }
};
