import java.util.*;

class Solution {
    // Author     : subas-mohanty
    // Date       : 07-10-2025
    // Problem Id : Leetcode 102
    // TC : O(N) --> We are visiting every node at most once
    // SC : O(N + 2^h-1) --> N for the result list and we are also using a queue which will store the maximum number of nodes at a level in the binary tree. And in a binary tree the maximum no. of nodes is present in the last level. i.e, 2^(height - 1)

    private static class TreeNode {
        public int val;
        public TreeNode left;
        public TreeNode right;
    }
    public List<List<Integer>> levelOrder(TreeNode root) {

        List<List<Integer>> result = new ArrayList<>();
        if(root == null) return result;

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while(!queue.isEmpty()){
            int levelSize = queue.size();
            List<Integer> level = new ArrayList<>();

            for(int i = 0; i < levelSize; i++){
                TreeNode node = queue.poll();
                level.add(node.val);

                if(node.left != null) queue.offer(node.left);
                if(node.right != null) queue.offer(node.right);
            }
            result.add(level);
        }
        return result;
    }
}