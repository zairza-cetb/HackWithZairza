/*
Problem: Invert Binary Tree

Description:
Given the root of a binary tree, invert the tree, and return its root.
  Example 1:
    Input: root = [4,2,7,1,3,6,9]
    Output: [4,7,2,9,6,3,1]


Approach:
Recursive Depth-First Search (DFS)
At every node in the tree:
  - Swap the left and right child nodes.
  - Recursively repeat this operation for the left and right subtrees.

Steps:
1. Base case:
  - If the current node is null, there's nothing to do, so return null.
  - This base case ensures the recursion stops when it reaches the leaves.
2. Swap the childeren:
  - Store the left child temporarily.
  - Assign the right child to root.left.
  - Assign the saved left child to root.right.
  - Now, the children of the current node are swapped.
3. Recursive inversion:
  - After swapping, now recursively invert the subtrees.
  - Since the children are already swapped, continue recursion on the newly assigned children.
4. Return the root:
  - Finally, return the current node after its subtree has been inverted.


Time Complexity: O(n)
- Every node is visited once.
- At each node, a constant-time operation (swap) is done.
- So, total time = O(n), where n is the number of nodes.


Space Complexity: O(h)
- h is the height of the tree.
- In a balanced tree, h = log(n) → O(log n)
- In a skewed tree, h = n → O(n)


Example:
  Input: root = [4,2,7,1,3,6,9]
  Output: [4,7,2,9,6,3,1]
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
    public TreeNode invertTree(TreeNode root) {
        if(root == null){
            return root;
        }
        TreeNode temp = root.left;
        root.left = root.right;
        root.right = temp;

        invertTree(root.left);
        invertTree(root.right);

        return root;
    }
}
