#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    
    int maxLen = 0;
    int current = 0;
    
    for (int i = 0; i < n; i++) {
        if (a[i] != 0) {
            current++;
            if (current > maxLen)
                maxLen = current;
        } else {
            current = 0; // reset when a zero appears
        }
    }
    
    cout << maxLen;
    return 0;
}
