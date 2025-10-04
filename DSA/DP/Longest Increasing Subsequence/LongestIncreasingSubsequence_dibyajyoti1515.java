/*
 * Author: Dibyajyoti Parida
 * 
 * Problem: Longest Increasing Subsequence
 * 
 * Approach:
 * 1. Use Dynamic Programming (Bottom-Up approach).
 * 2. Maintain an array `dp` where dp[i] = length of LIS ending at index i.
 * 3. For each index i, check all previous indices j (0 <= j < i):
 *      - if nums[i] > nums[j], update dp[i] = max(dp[i], dp[j] + 1)
 * 4. The answer is the maximum value in dp[].
 * 
 * Input: User enters the length of the array followed by the elements.
 * Output: Length of the longest increasing subsequence.
 * 
 * Time Complexity: O(n^2)
 * Space Complexity: O(n)
 */

import java.util.Scanner;
import java.util.Arrays;

public class LongestIncreasingSubsequence_dibyajyoti1515 {

    public static int lengthOfLIS(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n];
        Arrays.fill(dp, 1); // Every element is an LIS of length 1 by itself

        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
        }

        // Find the maximum value in dp[]
        int maxLength = 0;
        for (int len : dp) {
            maxLength = Math.max(maxLength, len);
        }
        return maxLength;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the length of the array: ");
        int n = sc.nextInt();
        int[] nums = new int[n];

        System.out.println("Enter the elements of the array:");
        for (int i = 0; i < n; i++) {
            nums[i] = sc.nextInt();
        }

        int result = lengthOfLIS(nums);
        System.out.println("Length of Longest Increasing Subsequence: " + result);
    }
}
