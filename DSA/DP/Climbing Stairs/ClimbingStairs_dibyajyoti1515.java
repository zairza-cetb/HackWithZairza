// Slove using Memoization
// Time Complexity: O(n)
// Space Complexity: O(n)

import java.util.Scanner;

public class ClimbingStairs_dibyajyoti1515 {

    public static int climbStairs(int n, int[] dp) {
        if ( n ==0 || n == 1 ) return 1;  // Base Case

        if ( dp[n] != 0 ) return dp[n];  // result already in dp array so return it

        dp[n] = climbStairs(n -1, dp) + climbStairs(n -2, dp); 

        return dp[n];
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();   // Input
        int[] dp = new int[n+1];   // Memoization Array
        
        System.out.println(climbStairs(n, dp));
    }
}