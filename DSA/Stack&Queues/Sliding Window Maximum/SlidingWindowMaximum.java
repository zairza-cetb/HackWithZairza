/*
Problem: Sliding Window Maximum
Description:
Given an array of integers nums and a sliding window of size k which moves from left to right,
return the maximum value in each window position.

Approach:
We use a Deque (Double-ended Queue) to efficiently track potential maximum values.
The deque stores indices of array elements in decreasing order of their values.

Key Insights:
1. We only care about elements that could potentially be the maximum in current or future windows
2. If a new element is larger than elements at the back of deque, those elements can never be maximum
3. Elements outside the current window (too far left) should be removed from the front

Deque Properties:
- Front of deque always contains the index of the maximum element in current window
- Elements are stored in decreasing order of their values
- We store indices (not values) to check if elements are still in the window

Steps:
1. Create a deque to store indices
2. Create result array of size (n - k + 1)
3. For each element in the array:
   a. Remove indices from front if they're outside current window (i - k)
   b. Remove indices from back while their values are smaller than current element
   c. Add current index to back of deque
   d. If window is complete (i >= k-1), add front element's value to result

Time and Space Complexity:
    - Time Complexity: O(n) — each element is added and removed from deque at most once
    - Space Complexity: O(k) — deque can have at most k elements

Example Walkthrough:
    Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
    
    i=0, nums[0]=1:  deque=[0]
    i=1, nums[1]=3:  deque=[1] (removed 0 because 1 < 3)
    i=2, nums[2]=-1: deque=[1,2], window complete → result[0] = nums[1] = 3
    
    i=3, nums[3]=-3: deque=[1,2,3], window complete → result[1] = nums[1] = 3
    i=4, nums[4]=5:  deque=[4] (removed all, 5 is largest), result[2] = 5
    i=5, nums[5]=3:  deque=[4,5], result[3] = nums[4] = 5
    i=6, nums[6]=6:  deque=[6] (removed 4,5), result[4] = 6
    i=7, nums[7]=7:  deque=[7] (removed 6), result[5] = 7
    
    Output: [3,3,5,5,6,7]
*/

class Solution {
  public int[] maxSlidingWindow(int[] nums, int k) {
    // Edge case: empty array
    if (nums == null || nums.length == 0) {
      return new int[0];
    }

    int n = nums.length;
    // Result array will have (n - k + 1) windows
    int[] result = new int[n - k + 1];
    int resultIndex = 0;

    // Deque stores indices of array elements
    // Elements are in decreasing order of their values
    Deque<Integer> deque = new ArrayDeque<>();

    // Process each element in the array
    for (int i = 0; i < n; i++) {
      // Remove indices that are outside the current window
      // Front of deque contains oldest element's index
      while (!deque.isEmpty() && deque.peekFirst() < i - k + 1) {
        deque.pollFirst();
      }

      // Remove indices from back whose values are smaller than current element
      // These elements can never be the maximum in current or future windows
      while (!deque.isEmpty() && nums[deque.peekLast()] < nums[i]) {
        deque.pollLast();
      }

      // Add current element's index to the back of deque
      deque.offerLast(i);

      // If we've processed at least k elements, record the maximum
      // The front of deque always contains the index of maximum element
      if (i >= k - 1) {
        result[resultIndex++] = nums[deque.peekFirst()];
      }
    }

    return result;
  }
}

/*
 * Visualization of Deque for nums = [1,3,-1,-3,5,3,6,7], k = 3:
 * 
 * Step-by-step:
 * i=0: [1] → deque indices: [0]
 * i=1: [1,3] → deque indices: [1] (1 removed, 3 > 1)
 * i=2: [1,3,-1] → deque indices: [1,2] → max = 3 ✓
 * 
 * i=3: [3,-1,-3] → deque indices: [1,2,3] → max = 3 ✓
 * i=4: [-1,-3,5] → deque indices: [4] → max = 5 ✓ (all removed, 5 is largest)
 * i=5: [-3,5,3] → deque indices: [4,5] → max = 5 ✓
 * i=6: [5,3,6] → deque indices: [6] → max = 6 ✓
 * i=7: [3,6,7] → deque indices: [7] → max = 7 ✓
 * 
 * Why this works:
 * - Deque front always has the maximum because we maintain decreasing order
 * - We remove smaller elements from back because they can't be future maximums
 * - We remove out-of-window elements from front to keep deque valid
 */
