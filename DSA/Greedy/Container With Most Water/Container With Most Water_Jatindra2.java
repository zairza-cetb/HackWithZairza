/*
Problem: Container With Most Water

Description:
  You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
  Find two lines that together with the x-axis form a container, such that the container contains the most water.
  Return the maximum amount of water a container can store.
  Notice that you may not slant the container.

Approach:
  Two-Pointer Technique
  Steps:
    1. Initialize pointers and variables:
        - lh (left pointer) = 0 (start of the array)
        - rh (right pointer) = n - 1 (end of the array)
        - max_water = 0 to keep track of the maximum area found
    2. Loop while lh < rh:
        - Calculate the width between the two lines: wd = rh - lh
        - Determine the height of the container: h = Math.min(height[lh], height[rh])
        - Calculate the current area: area = h * wd
        - Update max_water with the maximum of current area and previously recorded max
    3. Move pointers:
        - If height[lh] < height[rh], increment lh (move left pointer to the right)
        - Else, decrement rh (move right pointer to the left)
        - This moves the pointer that points to the shorter line, trying to find a taller line that could increase the container area
    4. Return:
        - After the loop ends, return max_water which is the maximum water container area found

Time Complexity: O(n)
  - Because each pointer moves inward at most n times, so the total iterations are linear.
Space Complexity: O(1)
  - You only use a few variables regardless of the input size, no extra data structures.

Example:
  - Input: height = [1,8,6,2,5,4,8,3,7]
  - Output: 49

*/

import java.util.*;
class Solution {
    public int maxArea(int[] height) {
        int max_water = 0;
        int n = height.length;
        int lh = 0;
        int rh = n-1;
        while(lh<rh){
            int wd = rh-lh;
            int h = Math.min(height[lh], height[rh]);
            max_water = Math.max(max_water, h*wd);
            if(height[lh]<height[rh]){
                lh++;
            }else{
                rh--;
            }
        }
        return max_water;
    }
}
