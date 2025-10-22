// Definition for a binary tree node.
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
        left = null;
        right = null;
    }
}

public class PathSum {

    /**
     * Returns true if the tree has a root-to-leaf path such that
     * adding up all the values along the path equals targetSum.
     * 
     * @param root      The root node of the binary tree.
     * @param targetSum The target sum to check against.
     * @return true if such a path exists, false otherwise.
     */
    public boolean hasPathSum(TreeNode root, int targetSum) {
        // If the current node is null, no path exists.
        if (root == null) {
            return false;
        }

        // If we are at a leaf node, check if the node's value equals targetSum.
        if (root.left == null && root.right == null) {
            return root.val == targetSum;
        }

        // Recursively check the left and right subtree with the reduced targetSum.
        return hasPathSum(root.left, targetSum - root.val) || hasPathSum(root.right, targetSum - root.val);
    }

    // Example usage
    public static void main(String[] args) {
        // Constructing the example tree:
        //          5
        //         / \
        //        4   8
        //       /   / \
        //      11  13  4
        //     /  \      \
        //    7    2      1

        TreeNode root = new TreeNode(5);

        root.left = new TreeNode(4);
        root.right = new TreeNode(8);

        root.left.left = new TreeNode(11);
        root.left.left.left = new TreeNode(7);
        root.left.left.right = new TreeNode(2);

        root.right.left = new TreeNode(13);
        root.right.right = new TreeNode(4);
        root.right.right.right = new TreeNode(1);

        PathSum solution = new PathSum();

        int targetSum = 22;
        boolean result = solution.hasPathSum(root, targetSum);

        System.out.println("Has path sum of " + targetSum + "? " + result);
        // Expected output: true (because 5->4->11->2 sums to 22)
    }
}
