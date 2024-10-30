#include <bits/stdc++.h>
using namespace std;

// Definition of the TreeNode structure
struct TreeNode {
    int value;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int val) : value(val), left(nullptr), right(nullptr) {}
};

// Function to insert nodes into the binary tree in level order
TreeNode* insert(vector<int>& arr, TreeNode* root, int i, int n) {
    // If the current index is within the bounds of the array
    if (i < n) {
        // Create a new TreeNode with the current value
        TreeNode* tmp = new TreeNode(arr[i]);
        root = tmp;

        // Recursively insert the left child
        root->left = insert(arr, root->left, 2 * i + 1, n);

        // Recursively insert the right child
        root->right = insert(arr, root->right, 2 * i + 2, n);
    }
    return root;
}

// Function to calculate the max depth of a binary tree
int maxDepth(TreeNode* root) {
    // Base case: if the node is null, return 0
    if (root == nullptr) return 0;

    // Recursively find the height of the left subtree
    int lh = maxDepth(root->left);

    // Recursively find the height of the right subtree
    int rh = maxDepth(root->right);

    // return the maximum max depth found so far
    return 1 + max(lh, rh);
}


int main() {
    int n;
    cout << "Enter no. of Nodes: ";
    cin >> n;

    vector<int> tree(n);
    cout << "Enter the nodes: ";
    for (int i = 0; i < n; i++) {
        cin >> tree[i];
    }

    // Construct the binary tree
    TreeNode* root = nullptr;
    root = insert(tree, root, 0, n);

    // Find and print the max depth of the tree
    cout <<maxDepth(root) << endl;

    return 0;
}

//Example:

//input :
//Enter no. of Nodes : 5
// 1 2 3 4 5

//output :
// 3
