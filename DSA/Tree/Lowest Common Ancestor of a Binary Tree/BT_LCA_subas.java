class Solution {
    // Author     : subas-mohanty
    // Date       : 07-10-2025
    // Problem Id : Leetcode 236
    // Link       : https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree
    // TC : O(N) --> visiting all nodes only once
    // SC : O(h) --> height of the binary tree due to the recursion stack space

    private static class TreeNode {
        TreeNode left;
        TreeNode right;
    }

    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(root == null || root == p || root == q) return root; // if either of the node is found then return that node

        // left will store either of the node is present on the left hand side of the current node or null if neither of the node is found
        TreeNode left = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);

        if(left != null && right != null) return root; // this is the parent node because in this node's left and right p and q are present

        if(left == null) return right; // left = null means either of the nodes is not present in the left hand side of the current node so both the node p and q are present on the right hand side
        return left; // this means right = null and both the nodes present on the left hand side
    }
}