class Node
{
    Integer value;
    Node left, right;

    Node(Integer val)
    {
        value = val;
        left = right = null;
    }
}

class BinaryTree
{
    Node root;
    int maxDepth(Node root)
    {
        // Root being null means tree doesn't exist.
        if (root == null)
            return 0;

        // Get the depth of the left and right subtree
        // using recursion.
        int leftDepth = maxDepth(root.left);
        int rightDepth = maxDepth(root.right);

        // Choose the larger one and add the root to it.
        if (leftDepth > rightDepth)
            return (leftDepth + 1);
        else
            return (rightDepth + 1);
    }

    // Driver code
    public static void main(String[] args)
    {
        BinaryTree tree = new BinaryTree();
        tree.root = new Node(3);
        tree.root.left = new Node(9);
        tree.root.right = new Node(20);
        tree.root.left.left = new Node(null);
        tree.root.left.right = new Node(null);
        tree.root.right.left = new Node(15);
        tree.root.right.right = new Node(7);

        System.out.println("Max depth: " + tree.maxDepth(tree.root));
    }
} 