#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;
    while (T--) {
        long long C, X, Y;
        cin >> C >> X >> Y;
        long long need = C - X;
        long long cost = need * Y;
        cout << cost << endl;
    }
    return 0;
}
