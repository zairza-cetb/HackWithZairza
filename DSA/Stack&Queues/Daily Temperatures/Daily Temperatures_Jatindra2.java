/*
Problem: Daily Temperatures

Description: 
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
  Example 1:
  Input: temperatures = [73,74,75,71,69,72,76,73]
  Output: [1,1,4,2,1,1,0,0]


Explaination:
We are given a list of daily temperatures. For each day, we need to figure out how many days we have to wait until a warmer temperature.
If there is no future day with a warmer temperature, we just put 0.


Approach:
We use a monotonic decreasing stack to keep track of the indices of days with unresolved temperatures (i.e., temperatures that haven't yet found a warmer future day).
Steps:
  1.Initialize:
    - An empty stack to store indices of the temperatures array.
    - An answer array of the same length, initialized to all zeros (default in Java).
  2.Iterate over the temperatures:
      - For each day i, while the current temperature temperatures[i] is greater than the temperature at the top of the stack (i.e., temperatures[stack.peek()]):
          - Pop the index prevIndex from the stack.
          - Set answer[prevIndex] = i - prevIndex, as day i is the first warmer day after prevIndex.
      - Push the current index i onto the stack.
  3. Result:
      - Any indices left in the stack do not have a warmer day in the future, so their default value in the answer array remains 0.


Time Complexity: O(n)
  - Each index is pushed and popped at most once.
  - So the total operations across the array are linear.
Space Complexity: O(n)
  - The stack stores up to n indices in the worst case (strictly decreasing temperatures).
  - The output array also uses O(n) space.


Example:
  Input: temperatures = [30,40,50,60]
  Output: [1,1,1,0]

*/

import java.util.*;
class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        // Stack to store indices of days with unresolved warmer temperatures
        Stack<Integer> temp = new Stack<>();
        int n = temperatures.length;
        // Result array to store number of days to wait for a warmer temperature
        int answer[] = new int[n];
        for(int i = 0; i<n; i++){
            // Check if current temperature is warmer than the temperature at index on top of stack
            while(!temp.isEmpty() && temperatures[i] > temperatures[temp.peek()]){
                int top = temp.pop();
                answer[top] = i-top;  // Calculate how many days we had to wait
            }
            temp.push(i);  // Push current day's index to the stack
        }
        // Any indices left in the stack will have default value 0 in ans[] (no warmer day ahead)
        return answer;
    }
}
