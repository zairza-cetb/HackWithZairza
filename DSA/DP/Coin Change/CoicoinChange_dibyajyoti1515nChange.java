/*
 * Author: Dibyajyoti Parida
 * 
 * Problem: Coin Change
 * 
 * Approach:
 * 1. Use Dynamic Programming (Top-Down approach with Memoization).
 * 2. For each amount, recursively try using each coin and find the minimum number of coins.
 * 3. Use a memo array to store results for amounts already computed to avoid recomputation.
 * 
 * Input: User enters the number of coin types, the coin denominations, and the total amount.
 * Output: Minimum number of coins required (or -1 if impossible).
 * 
 * Time Complexity: O(amount * n), where n = number of coins.
 *   - Each subproblem for amount 'amt' is computed only once.
 *   - For each subproblem, we try all 'n' coins.
 * Space Complexity: O(amount) for memoization array + O(amount) for recursion stack.
 */



 
import java.util.Arrays;
import java.util.Scanner;

public class CoicoinChange_dibyajyoti1515nChange {

    // Memoization array
    static int[] memo;

    public static int coinChange(int[] coins, int amount) {

        // Initialize memo array with -2
        memo = new int[amount + 1];
        Arrays.fill(memo, -2);
        return dp(coins, amount);
    }

    // Recursive function with memoization
    static int dp(int[] coins, int amt) {

        // Base case
        if (amt == 0) return 0;

        // If amount < 0, not possible
        if (amt < 0) return -1;

        // Return memoized result if already computed
        if (memo[amt] != -2) return memo[amt];

        int minCoins = Integer.MAX_VALUE;

        for (int coin : coins) {
            int res = dp(coins, amt - coin);
            if (res >= 0) { 
                minCoins = Math.min(minCoins, res + 1);
            }
        }

        // no valid
        memo[amt] = (minCoins == Integer.MAX_VALUE) ? -1 : minCoins;
        return memo[amt];
    }

    // Example run
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Input number of coins
        System.out.print("Enter number of coin types: ");
        int n = sc.nextInt();
        int[] coins = new int[n];

        // Input coin denominations
        System.out.println("Enter the coin denominations:");
        for (int i = 0; i < n; i++) {
            coins[i] = sc.nextInt();
        }

        // Input amount
        System.out.print("Enter the amount: ");
        int amount = sc.nextInt();

        int result = coinChange(coins, amount);
        System.out.println("Minimum number of coins required: " + result);
    }
}
