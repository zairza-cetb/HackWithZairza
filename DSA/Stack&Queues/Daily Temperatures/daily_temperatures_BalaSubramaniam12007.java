/*
Problem: Daily Temperatures

Description:
Given an array of integers 'temperatures' representing daily temperatures, 
return an array 'res' such that res[i] is the number of days you have to wait 
until a warmer temperature. If there is no future day with a warmer temperature, put 0 instead.

Example:
Input: temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
Output: [1, 1, 4, 2, 1, 1, 0, 0]

Constraints:
1 <= temperatures.length <= 10^5
30 <= temperatures[i] <= 100


Approach:
We solve this problem efficiently using a **Monotonic Stack**.

A monotonic stack is a stack that keeps its elements in sorted order (in this case, decreasing temperature order).
The key idea is:
1. Iterate through each temperature.
2. For each temperature, compare it with the top of the stack.
   - While the current temperature is greater than the temperature at the top of the stack,
     it means we've found a warmer day for that previous temperature.
   - Pop the stack, calculate the difference in indices, and store it in the result array.
3. Push the current temperature and its index onto the stack.
4. Continue until the end of the array.

By the end, all indices remaining in the stack have no warmer days ahead, so their result remains 0.


Steps:
1. Initialize a result array 'res' of the same length as 'temperatures'.
2. Create an empty stack to store pairs [temperature, index].
3. Traverse the 'temperatures' array:
   - While stack is not empty and current temperature is greater than the top of stack temperature:
       - Pop the stack.
       - Calculate days waited = current index - popped index.
       - Store the result in 'res' for that popped index.
   - Push the current [temperature, index] pair to stack.
4. Return the 'res' array.


Time and Space Complexity:
- Time Complexity: O(n)
  Each temperature is pushed and popped at most once.
- Space Complexity: O(n)
  Stack can hold up to n elements in the worst case.

Example walkthrough:
Input: [73, 74, 75, 71, 69, 72, 76, 73]

Step by step:
Index 0: temp = 73, push [73,0]
Index 1: temp = 74, 74 > 73 => pop [73,0], res[0] = 1, push [74,1]
Index 2: temp = 75, 75 > 74 => pop [74,1], res[1] = 1, push [75,2]
Index 3: temp = 71, push [71,3]
Index 4: temp = 69, push [69,4]
Index 5: temp = 72, 72 > 69 => pop [69,4], res[4] = 1
            72 > 71 => pop [71,3], res[3] = 2, push [72,5]
Index 6: temp = 76, pop [72,5], res[5] = 1; pop [75,2], res[2] = 4; push [76,6]
Index 7: temp = 73, push [73,7]

Final res = [1, 1, 4, 2, 1, 1, 0, 0]

*/

import java.util.*;

public class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int[] res = new int[temperatures.length];
        Stack<int[]> stack = new Stack<>(); // pair: [temperature, index]

        for (int i = 0; i < temperatures.length; i++) {
            int currentTemp = temperatures[i];
            // Check if current temperature is warmer than the last one in stack
            while (!stack.isEmpty() && currentTemp > stack.peek()[0]) {
                int[] prev = stack.pop();
                int prevIndex = prev[1];
                res[prevIndex] = i - prevIndex; // Calculate the number of days waited
            }
            stack.push(new int[]{currentTemp, i}); // Push current temp and its index
        }

        return res;
    }
}

// Time Complexity: O(n) — Each temperature is pushed and popped once.
// Space Complexity: O(n) — For the stack storing temperatures and indices.
