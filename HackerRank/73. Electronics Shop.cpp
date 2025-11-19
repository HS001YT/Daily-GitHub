#include <bits/stdc++.h>
using namespace std;

int getMoneySpent(vector<int> keyboards, vector<int> drives, int b) {
    int best = -1;

    for (int k : keyboards) {
        for (int d : drives) {
            int total = k + d;
            if (total <= b && total > best) {
                best = total;
            }
        }
    }

    return best;
}