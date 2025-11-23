#include<bits/stdc++.h>
using namespace std;

vector<int> countingSort(vector<int> arr) {
    vector<int> freq(100, 0);

    for (int num : arr) {
        freq[num]++;
    }

    return freq;
}