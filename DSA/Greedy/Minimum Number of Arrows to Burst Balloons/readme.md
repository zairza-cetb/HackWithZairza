## Problem 3: Minimum Number of Arrows to Burst Balloons
There are some spherical balloons taped onto a wall. Each balloon is represented as [start, end] coordinates. An arrow shot vertically can burst all balloons whose coordinates overlap with it. Find the minimum number of arrows needed to burst all balloons.

### Example:
```
Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
```
Explanation: One arrow at x = 6 bursts [2,8], [1,6], and [7,12].
Another at x = 11 bursts [10,16].


### Constraints:
- `1 <= points.length <= 10^5`
- `points[i].length == 2`

### Source: [LeetCode #452](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)
