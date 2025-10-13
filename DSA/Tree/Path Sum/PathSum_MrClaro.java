/*
Problem: Path Sum
Description:
Given the root of a binary tree and an integer targetSum, return true if the tree has a 
root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Approach:
We use a recursive approach to traverse the tree and check if there exists a path from root 
to any leaf whose sum equals targetSum.

The key insight is that at each node, we subtract the current node's value from targetSum 
and pass the remaining sum to the child nodes. When we reach a leaf node, we check if the 
remaining sum equals the leaf's value.

Steps:
1. Base Case - Empty Tree:
    - If root is null, return false (no path exists)

2. Base Case - Leaf Node:
    - If current node is a leaf (no left and no right child)
    - Check if targetSum equals the current node's value
    - If yes, we found a valid path, return true

3. Recursive Case:
    - Subtract current node's value from targetSum
    - Recursively check left subtree with (targetSum - node.val)
    - Recursively check right subtree with (targetSum - node.val)
    - Return true if either left OR right subtree has a valid path

Time and Space Complexity:
    - Time Complexity: O(n) — we visit each node exactly once in worst case
    - Space Complexity: O(h) — where h is the height of the tree (recursion stack)
      In worst case (skewed tree): O(n)
      In best case (balanced tree): O(log n)

Example:
    Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
    
           5
          / \
         4   8
        /   / \
       11  13  4
      / \       \
     7   2       1
    
    Path: 5 -> 4 -> 11 -> 2
    Check 5: targetSum = 22, continue with 22-5 = 17
    Check 4: targetSum = 17, continue with 17-4 = 13
    Check 11: targetSum = 13, continue with 13-11 = 2
    Check 2 (leaf): targetSum = 2, node.val = 2 ✓
    Output: true
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
  public boolean hasPathSum(TreeNode root, int targetSum) {
    // Base case: if tree is empty, no path exists
    if (root == null) {
      return false;
    }

    // Base case: if current node is a leaf node
    // Check if the remaining targetSum equals the leaf's value
    if (root.left == null && root.right == null && targetSum == root.val) {
      return true;
    }

    // Recursive case: check left and right subtrees
    // Subtract current node's value from targetSum and pass to children
    // Return true if either left OR right subtree has a valid path
    return hasPathSum(root.left, targetSum - root.val) ||
        hasPathSum(root.right, targetSum - root.val);
  }
}
// As we visit each node exactly once during the recursion, time complexity is
// O(n)
