/*
 * Author: Dibyajyoti Parida
 * 
 * Problem: Container With Most Water (LeetCode #11)
 * 
 * Approach:
 * 1. Use two pointers, left and right, starting at both ends of the array.
 * 2. Calculate area formed by lines at left and right.
 * 3. Move the pointer with the smaller height inward to potentially find a bigger area.
 * 4. Track and return the maximum area.
 * 
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */



 
import java.util.Scanner;

public class ContainerWithMostWater_dibyajyoti1515 {

    public static int maxArea(int[] height) {
        int left = 0, right = height.length - 1;
        int maxArea = 0;

        while (left < right) {
            int width = right - left;
            int currentHeight = Math.min(height[left], height[right]);
            int area = width * currentHeight;
            maxArea = Math.max(maxArea, area);

            // Move the smaller height inward
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
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