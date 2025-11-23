#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;
    
    while (t--) {
        long long n;
        cin >> n;
        
        long long sum = 0;
        for (long long i = 1; i <= n; i += 2) {
            sum += (n - i + 1) * (n - i + 1);
        }
        
        cout << sum << endl;
    }
    
    return 0;
}