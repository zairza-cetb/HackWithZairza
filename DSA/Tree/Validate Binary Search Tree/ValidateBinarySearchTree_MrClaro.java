/*
Problem: Validate Binary Search Tree
Description:
Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
1. The left subtree of a node contains only nodes with keys less than the node's key.
2. The right subtree of a node contains only nodes with keys greater than the node's key.
3. Both the left and right subtrees must also be binary search trees.

Approach:
To validate a BST, we need to ensure that every node follows the BST property. A common mistake 
is to only check if left child < node < right child. This is insufficient because we need to ensure 
ALL nodes in the left subtree are less than the current node, and ALL nodes in the right subtree 
are greater.

We use a recursive approach with range validation:
- Each node must fall within a valid range [min, max]
- For the root, the range is [-∞, +∞]
- For left children, update the max bound to parent's value
- For right children, update the min bound to parent's value

Steps:
1. Start with the root node and initial range [-∞, +∞]
2. For Each Node:
    - Check if the node's value is within the valid range (min < node.val < max)
    - If not, return false
3. Recursively Validate:
    - Left subtree with updated range [min, node.val]
    - Right subtree with updated range [node.val, max]
4. Base Case:
    - If node is null, return true (empty tree is valid BST)

Time and Space Complexity:
    - Time Complexity: O(n) — we visit each node exactly once
    - Space Complexity: O(h) — where h is the height of the tree (recursion stack)
      In worst case (skewed tree): O(n)
      In best case (balanced tree): O(log n)

Example:
    Input: root = [2,1,3]
         2
        / \
       1   3
    
    Check 2: range [-∞, +∞] ✓
    Check 1: range [-∞, 2] ✓
    Check 3: range [2, +∞] ✓
    Output: true
    
    Input: root = [5,1,4,null,null,3,6]
         5
        / \
       1   4
          / \
         3   6
    
    Check 5: range [-∞, +∞] ✓
    Check 1: range [-∞, 5] ✓
    Check 4: range [5, +∞] ✗ (4 < 5, invalid!)
    Output: false
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
  public boolean isValidBST(TreeNode root) {
    // Start validation with full range: (-∞, +∞)
    // Using null to represent infinity
    return validate(root, null, null);
  }

  // Helper method to validate BST with range constraints
  // min: minimum value the current node can have (exclusive)
  // max: maximum value the current node can have (exclusive)
  private boolean validate(TreeNode node, Integer min, Integer max) {
    // Base case: empty tree is a valid BST
    if (node == null) {
      return true;
    }

    // Check if current node's value violates min constraint
    if (min != null && node.val <= min) {
      return false;
    }

    // Check if current node's value violates max constraint
    if (max != null && node.val >= max) {
      return false;
    }

    // Recursively validate left subtree with updated max bound
    // All nodes in left subtree must be less than current node's value
    boolean leftValid = validate(node.left, min, node.val);

    // Recursively validate right subtree with updated min bound
    // All nodes in right subtree must be greater than current node's value
    boolean rightValid = validate(node.right, node.val, max);

    // Both subtrees must be valid for the tree to be a valid BST
    return leftValid && rightValid;
  }
}
// As we visit each node exactly once during the recursion, time complexity is
// O(n)
