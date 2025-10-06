/*
 * Author: Dibyajyoti Parida
 * 
 * Problem: Container With Most Water (LeetCode #11)
 * 
 * Greedy Two-Pointer Approach:
 * 1. Initialize two pointers, left and right, at both ends of the array.
 * 2. Calculate the area between the two lines (width × min(height[left], height[right])).
 * 3. Keep track of the maximum area encountered.
 * 4. Apply a greedy decision:
 *    - Move the pointer with the smaller height inward,
 *      since moving the taller one won't increase the area.
 * 5. Repeat until both pointers meet.
 * 6. Return the maximum area obtained.
 * 
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */

import java.util.Scanner;

public class ContainerWithMostWater_dibyajyoti1515 {

    public static int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int maxArea = 0;

        while (left < right) {
            int width = right - left;
            int currentHeight = Math.min(height[left], height[right]);
            int area = width * currentHeight;
            maxArea = Math.max(maxArea, area);

            // Greedy move: shift the smaller height inward
            if (height[left] < height[right]) {
                left++;  // Move left pointer rightward to find a taller line
            } else {
                right--; // Move right pointer leftward to find a taller line
            }
        }

        return maxArea;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of lines: ");
        int n = sc.nextInt();
        int[] height = new int[n];

        System.out.println("Enter heights:");
        for (int i = 0; i < n; i++) {
            height[i] = sc.nextInt();
        }

        int result = maxArea(height);
        System.out.println("Maximum water container area: " + result);
    }
}
