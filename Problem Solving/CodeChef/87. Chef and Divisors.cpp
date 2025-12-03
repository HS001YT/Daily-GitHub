#include <bits/stdc++.h>
using namespace std;
using int64 = long long;

// Memoization map to store score of numbers
unordered_map<int64,int64> dp;

// Count number of proper divisors of n
int64 countProperDivisors(int64 n) {
    if(n == 1) return 0;
    int64 cnt = 0;
    for(int64 i=1; i*i <= n; i++) {
        if(n % i == 0) {
            if(i != n) cnt++;               // i is a proper divisor
            int64 j = n / i;
            if(j != i && j != n) cnt++;     // n/i is a proper divisor
        }
    }
    return cnt;
}

// Compute score of number n
int64 score(int64 n) {
    if(n == 1) return 0;  // leaf
    if(dp.count(n)) return dp[n];
    
    int64 best = 0;
    
    // Iterate all proper divisors
    for(int64 i=1; i*i <= n; i++) {
        if(n % i == 0) {
            if(i != n) best = max(best, score(i));
            int64 j = n / i;
            if(j != i && j != n) best = max(best, score(j));
        }
    }
    
    dp[n] = best + countProperDivisors(n);
    return dp[n];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int64 A, B;
    cin >> A >> B;
    
    int64 ans = 0;
    for(int64 n = A; n <= B; n++) {
        ans += score(n);
    }
    
    cout << ans << "\n";
    return 0;
}
