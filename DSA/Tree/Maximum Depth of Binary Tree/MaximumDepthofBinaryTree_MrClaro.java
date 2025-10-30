/*
Problem: Maximum Depth of Binary Tree
Description:
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the 
root node down to the farthest leaf node.

Approach:
We use a recursive approach to traverse the tree and calculate the maximum depth.
The key insight is that the depth of a tree is 1 (current node) plus the maximum depth 
of its subtrees.

Steps:
1. Base Case - Empty Tree:
    - If root is null, return 0 (no depth)

2. Recursive Case:
    - Recursively calculate the depth of the left subtree
    - Recursively calculate the depth of the right subtree
    - Return 1 (current node) + maximum of (left depth, right depth)

Time and Space Complexity:
    - Time Complexity: O(n) — we visit each node exactly once
    - Space Complexity: O(h) — where h is the height of the tree (recursion stack)
      In worst case (skewed tree): O(n)
      In best case (balanced tree): O(log n)

Example:
    Input: root = [3,9,20,null,null,15,7]
    
           3
          / \
         9  20
           /  \
          15   7
    
    Execution:
    maxDepth(3): 
        - maxDepth(9) = 1 (leaf node, no children)
        - maxDepth(20):
            - maxDepth(15) = 1 (leaf node)
            - maxDepth(7) = 1 (leaf node)
            - return 1 + max(1, 1) = 2
        - return 1 + max(1, 2) = 3
    
    Output: 3
*/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode() {}
 * TreeNode(int val) { this.val = val; }
 * TreeNode(int val, TreeNode left, TreeNode right) {
 * this.val = val;
 * this.left = left;
 * this.right = right;
 * }
 * }
 */
class Solution {
  public int maxDepth(TreeNode root) {
    // Base case: if tree is empty, depth is 0
    if (root == null) {
      return 0;
    }

    // Recursive case: calculate depth of left and right subtrees
    // Return 1 (current node) + maximum depth of subtrees
    return Math.max(maxDepth(root.left), maxDepth(root.right)) + 1;
  }
}

// As we visit each node exactly once during the recursion, time complexity is
// O(n)
