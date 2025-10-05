/*
 * Author: Dibyajyoti Parida
 * 
 * Problem: Partition Equal Subset Sum
 * 
 * Approach:
 * 1. The problem can be reduced to finding whether there exists a subset
 *    whose sum equals half of the total array sum.
 * 2. If the total sum is odd, it’s impossible to divide it into two equal parts.
 * 3. Use Dynamic Programming (Bottom-Up) to check whether a subset with 
 *    target sum = totalSum / 2 exists.
 * 4. dp[i][j] represents whether a subset of the first i elements can achieve sum j.
 * 
 * Input: User enters the size of array and elements.
 * Output: true if partition possible, otherwise false.
 * 
 * Time Complexity: O(n * target)
 *   - n = number of elements, target = totalSum / 2
 * Space Complexity: O(target)
 *   - Optimized to 1D array to save space.
 */




 
import java.util.Scanner;

public class PartitionEqualSubsetSum_dibyajyoti1515 {

    public static boolean canPartition(int[] nums) {
        int totalSum = 0;
        for (int num : nums) totalSum += num;

        // If sum is odd, can not partition equally
        if (totalSum % 2 != 0) return false;

        int target = totalSum / 2;
        boolean[] dp = new boolean[target + 1];
        dp[0] = true; // Base case: sum 0 always possible

        for (int num : nums) {
            for (int j = target; j >= num; j--) {
                dp[j] = dp[j] || dp[j - num];
            }
        }

        return dp[target];
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of elements: ");
        int n = sc.nextInt();  
        int[] nums = new int[n];

        System.out.println("Enter the elements:"); // Input 
        for (int i = 0; i < n; i++) {
            nums[i] = sc.nextInt();
        }

        boolean result = canPartition(nums);  // Output
        System.out.println("Can partition equally? " + result);
    }
}
