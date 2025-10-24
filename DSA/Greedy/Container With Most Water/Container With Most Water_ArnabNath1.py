"""
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
        - left = 0 (start of the array)
        - right = n - 1 (end of the array)
        - max_water = 0 to keep track of the maximum area found
    2. Loop while left < right:
        - Calculate the width between the two lines: width = right - left
        - Determine the height of the container: h = min(height[left], height[right])
        - Calculate the current area: area = h * width
        - Update max_water with the maximum of current area and previously recorded max
    3. Move pointers:
        - If height[left] < height[right], increment left (move left pointer to the right)
        - Else, decrement right (move right pointer to the left)
        - This moves the pointer that points to the shorter line, trying to find a taller line that could increase the container area
    4. Return:
        - After the loop ends, return max_water which is the maximum water container area found

Time Complexity: O(n)
  - Each pointer moves inward at most n times, so the total iterations are linear.
Space Complexity: O(1)
  - Only a few variables are used regardless of input size.

Example:
  - Input: height = [1,8,6,2,5,4,8,3,7]
  - Output: 49
"""

class Solution:
    def maxArea(self, height):
        max_water = 0
        left = 0
        right = len(height) - 1

        while left < right:
            width = right - left
            h = min(height[left], height[right])
            area = h * width
            max_water = max(max_water, area)

            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water
