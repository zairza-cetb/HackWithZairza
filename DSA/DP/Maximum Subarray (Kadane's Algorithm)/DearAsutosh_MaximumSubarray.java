/**
 * Author: DearAsutosh
 * Problem: Maximum Subarray (Kadane's Algorithm) (LeetCode #53)
 * Description: Find the subarray with the largest sum in a given integer array.
 * 
 */

public class DearAsutosh_MaximumSubarray {

    /*
      =============================EASY EXPLANATION============================
      Given an integer array arr[], we have to find the subarray (containing at
      least one element) which has the maximum possible sum, and return that sum.
     */

    // return sum of maximum subarray
    public static int maxSubArray(int[] nums) {
        int maxSum = nums[0]; // Max sum found so far
        int currentSum = nums[0]; // Current subarray sum

        // DP relation: currentSum = max(nums[i], currentSum + nums[i])
        for (int i = 1; i < nums.length; i++) {
            currentSum = Math.max(nums[i], currentSum + nums[i]);
            maxSum = Math.max(maxSum, currentSum); // Update maxSum
        }

        return maxSum;
    }

    // if anyone find the above logic overwhelming, check this
    // easy-to-understand explanation of Kadane's Algorithm:
    // Link: https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/

    public static void main(String[] args) {
        int[] nums = { -2, 1, -3, 4, -1, 2, 1, -5, 4 };
        System.out.println("Maximum Subarray Sum = " + maxSubArray(nums));
    }
}
