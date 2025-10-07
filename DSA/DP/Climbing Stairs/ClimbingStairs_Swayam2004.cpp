/*
Approach:
1. Similar to the fibonacci series problem, where each problem can be divided into overlapping sub-problems
2. The no. of steps required is the sum of steps for the previous stair and the one before that

Time and Space Complexity:
TC: O(n)
SC: O(n)
where n = no. of stairs
*/

#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    vector<int> dp(n);
    dp[0] = 1;
    if (n >= 2) dp[1] = 2;

    for (int i=2; i<n; i++) {
        dp[i] = dp[i-1] + dp[i-2];
    }

    cout << dp[n-1] << "\n";
    
    return 0;
}
