# Minimal Cost
There is an array arr of heights of stone and Geek is standing at the first stone and can jump to one of the following: Stone i+1, i+2, ... i+k stone, where k is the maximum number of steps that can be jumped and cost will be |hi-hj| is incurred, where j is the stone to land on. Find the minimum possible total cost incurred before the Geek reaches the last stone.
### Example 1:
```
Input: k = 3, arr[]= [10, 30, 40, 50, 20]
Output: 30
Explanation: Geek will follow the path 1->2->5, the total cost would be 
|10-30| + |30-20| = 30, which is minimum
```
### Example 2:
```
Input: k = 1, arr[]= [10, 20, 10]
Output: 20
Explanation: Geek will follow the path 1->2->3, the total cost would be 
|10 - 20| + |20 - 10| = 20.
```
### Constraints:
* ```1<= arr.size() <=104```
* ```1 <= k <= 100```
* ```1 <= arr[i] <= 104```