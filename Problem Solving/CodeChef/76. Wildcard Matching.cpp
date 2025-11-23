#include <iostream>
#include <string>
using namespace std;

int main() {
    int t;
    cin >> t;
    
    while (t--) {
        string x, y;
        cin >> x >> y;
        
        bool match = true;
        int n = x.length();
        
        for (int i = 0; i < n; i++) {
            if (x[i] == '?' || y[i] == '?') {
                continue;
            }
            if (x[i] != y[i]) {
                match = false;
                break;
            }
        }
        
        if (match) {
            cout << "Yes" << endl;
        } else {
            cout << "No" << endl;
        }
    }
    
    return 0;
}