#include <bits/stdc++.h>
using namespace std;

int designerPdfViewer(vector<int> h, string word) {
    int maxHeight = 0;
    for (char c : word) {
        int height = h[c - 'a']; // get height for each character
        if (height > maxHeight)
            maxHeight = height;
    }
    return maxHeight * word.length();
}