#include <iostream>
#include <algorithm>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    int maxDepth(TreeNode* root) {
        if(root == nullptr) { 
            return 0;
        }
        int left = 1 + maxDepth(root->left);
        int right = 1 + maxDepth(root->right);
        return max(left, right);
    }
};

int main() {
    Solution solution;
  
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);

    int depth = solution.maxDepth(root);
    cout << "Max depth of the tree: " << depth << endl;

    return 0;
}
