/*
Problem: Validate Binary Search Tree

Description:
Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
  - The left subtree of a node contains only nodes with keys strictly less than the node's key.
  - The right subtree of a node contains only nodes with keys strictly greater than the node's key.
  - Both the left and right subtrees must also be binary search trees.


Approach:
The idea is to recursively traverse the tree and maintain a valid value range for each node. If any node breaks the BST rule, the function returns false.

Steps:
1. Initial call:
  - Start with the widest possible range.
  - Every node must be strictly between min and max.
2. Recursive Logic:
  - At each node:
    - Check if its value is within the allowed range.
    - If not, it violates the BST rule.
  - Then:
    - Recur left with new range: (min, root.val)
    - Recur right with new range: (root.val, max)
3. Update ranges:
  - For the left child, all values must be less than current node.
    - So we set the upper bound (max) to root.val.
  - For the right child, all values must be greater than current node.
    - So we set the lower bound (min) to root.val.
4. Base case:
  - An empty tree or subtree is always valid.


Time Complexity: O(n)
  - Where n is the number of nodes in the tree.
  - Every node is visited once.
  - Each visit performs constant-time checks and recursive calls.


Space Complexity: O(h)
  - Where h is the height of the tree.
  - This is due to the recursion stack (implicit space).
    - Best case (balanced tree): O(log n)
    - Worst case (skewed tree): O(n)


Example:
  Input: root = [2,1,3]
  Output: true
*/


/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isValid(TreeNode root, long min, long max){
        if(root == null){
            return true;
        }
        if(root.val >= max || root.val <= min){
            return false;
        }
        return isValid(root.left, min, root.val) && isValid(root.right, root.val, max);
    }
    public boolean isValidBST(TreeNode root) {
        return isValid(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }
}
