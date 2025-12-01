#include <bits/stdc++.h>
using namespace std;

int migratoryBirds(vector<int> arr) {
    vector<int> count(6, 0); // bird types are 1-5

    for (int x : arr) {
        count[x]++;
    }

    int mostCommon = 1;
    for (int i = 2; i <= 5; i++) {
        if (count[i] > count[mostCommon]) {
            mostCommon = i;
        }
    }

    return mostCommon;
}