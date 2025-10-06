/*
Approach 1:
1. Using top-down DP, to find the minimum coins required, at each step

Time and Space Complexity:
TC: O(S * n)
SC: O(n)
where n = amount, S = no. of coins

Approach 2:
1. Use bottom-up DP, to find the minimum coins required, starting from 0

Time and Space Complexity:
TC: O(S * n)
SC: O(n)
where n = amount, S = no. of coins
*/

#include <bits/stdc++.h>
using namespace std;

int dfs(vector<int>& coins, int amount, vector<int>& memo) {
    if (amount < 0) return -1;
    if (amount == 0) return 0;
    if (memo[amount] != -2) return memo[amount];
    
    int minCost = INT_MAX;

    for (int c : coins) {
        int res = dfs(coins, amount - c, memo);

        if (res >= 0 && res < minCost) {
            minCost = res + 1;
        }
    }

    memo[amount] = (minCost == INT_MAX) ? -1 : minCost;
    return memo[amount];
}

int coinChange(vector<int>& coins, int amount) {
    // // Approach 1 (Top-Down DP with Memo)
    // vector<int> memo(amount+1, -2);
    // return dfs(coins, amount, memo);

    // Approach 2 (Bottom-Up DP with Tabulation)
    vector<int> dp(amount+1, amount+1);
    dp[0] = 0;

    for (int i=1; i<=amount; i++) {
        for (int c : coins) {
            if (i - c < 0) continue;
            dp[i] = min(dp[i], dp[i-c] + 1);
        }
    }

    if (dp[amount] == amount+1) return -1;
    return dp[amount];
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin >> t;

    while (t--) {
        int n, a;
        cin >> n >> a;
    
        vector<int> coins(n);
        for (int& c : coins) cin >> c;
    
        cout << coinChange(coins, a) << "\n";
    }
    
    return 0;
}
