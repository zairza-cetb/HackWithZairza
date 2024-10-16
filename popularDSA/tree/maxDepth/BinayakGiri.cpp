#include <iostream>
#include <queue>

using namespace std;

// Definition of the TreeNode structure representing nodes of a binary tree.
struct TreeNode {
    int val; // Value stored in the node
    TreeNode *left; // Pointer to the left child of the node
    TreeNode *right; // Pointer to the right child of the node

    // Constructor to initialize the node
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

// Function to take user input to construct the binary tree in level order
TreeNode* buildTree() {
    int val;
    cout << "Enter the root node value (-1 for no node): ";
    cin >> val;

    if (val == -1) return nullptr;

    TreeNode* root = new TreeNode(val);
    queue<TreeNode*> q;
    q.push(root);

    // Level-order input for the binary tree
    while (!q.empty()) {
        TreeNode* current = q.front();
        q.pop();

        // Input left child
        cout << "Enter the left child of " << current->val << " (-1 for no node): ";
        cin >> val;
        if (val != -1) {
            current->left = new TreeNode(val);
            q.push(current->left);
        }

        // Input right child
        cout << "Enter the right child of " << current->val << " (-1 for no node): ";
        cin >> val;
        if (val != -1) {
            current->right = new TreeNode(val);
            q.push(current->right);
        }
    }

    return root;
}

// Solution class that contains the function to find the maximum depth of the binary tree.
class Solution {
public:
    // Optimized function for finding the maximum depth of a binary tree
    int maxDepth(TreeNode* root) {
        // If the tree is empty, return 0
        if (!root) return 0;

        // Use the recursive depth-first search (DFS) to compute depths
        return 1 + max(maxDepth(root->left), maxDepth(root->right));
    }
};

int main() {
    Solution solution; // Create an instance of the Solution class

    // Building the tree from user input
    cout << "Let's build the binary tree:\n";
    TreeNode* root = buildTree();

    // Call the maxDepth function to find the depth of the tree and store the result
    int depth = solution.maxDepth(root);

    // Print the maximum depth of the tree
    cout << "Max depth of the tree: " << depth << endl;

    return 0;
}
