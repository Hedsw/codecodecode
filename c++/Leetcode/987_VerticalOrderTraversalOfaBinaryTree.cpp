/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
/*
There is a similar problem Binary Tree Vertical Order Traversal, which is different from this problem only in the following requirement.
If two nodes are in the same row and column, the order should be from left to right.
In this problem, if two nodes are in the same row and column, the order should be from small to large.
The idea is to build a mapping from coordinates to nodes.
*/
// Time Compleixty - O(n*logn)
class Solution {
public:
    vector<vector<int>> verticalTraversal(TreeNode* root) {
        map<int, map<int, set<int>>> nodes;
        traverse(root, 0, 0, nodes);
        vector<vector<int>> ans;
        
        for(auto p : nodes) {
            vector<int> col;
            for (auto q : p.second) {
                col.insert(col.end(), q.second.begin(), q.second.end());
            }
            ans.push_back(col);
        }
        return ans; 
    }
    
private:
    void traverse(TreeNode* root, int x, int y, map<int, map<int, set<int>>>& nodes) {
        if(root) {
            nodes[x][y].insert(root->val);
            traverse(root->left, x-1, y+1, nodes);
            traverse(root->right, x+1, y+1, nodes);
        }
    }
};