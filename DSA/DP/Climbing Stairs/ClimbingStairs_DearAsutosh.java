/**
 * Author: DearAsutosh
 * Problem: Climbing Stairs (LeetCode #70)
 * Description: Find the number of distinct ways to climb n stairs
                when you can take 1 or 2 steps at a time.
 */
public class ClimbingStairs_DearAsutosh {
    // Return ways to climb n stairs
    public static int climbStairs(int n) {
        if (n <= 3)
            return n; // base case
        int firstPrev = 3, secPrev = 2, curr = 0;
        for (int i = 3; i < n; i++) {
            curr = firstPrev + secPrev; // DP relation: f(i) = f(i-1) + f(i-2)
            secPrev = firstPrev; // update previous values
            firstPrev = curr;
        }
        return curr;
    }

    public static void main(String[] args) {
        int n = 4;
        System.out.println("There are " + climbStairs(n) + " ways to climb " + n + " stairs.");
    }
}
