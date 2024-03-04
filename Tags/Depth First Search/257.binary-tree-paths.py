#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#
# https://leetcode.com/problems/binary-tree-paths/description/
#
# algorithms
# Easy (63.28%)
# Likes:    6421
# Dislikes: 281
# Total Accepted:    700.7K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,3,null,5]'
#
# Given the root of a binary tree, return all root-to-leaf paths in any order.
# 
# A leaf is a node with no children.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]
# 
# 
# Example 2:
# 
# 
# Input: root = [1]
# Output: ["1"]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 100].
# -100 <= Node.val <= 100
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        self.dfs(root, "", res)
        return res
    
    def dfs(self, root, path, res):
        if root:
            if not root.right and not root.left:
                res.append(path + str(root.val))
            
            self.dfs(root.left, path + str(root.val) + "->", res)
            self.dfs(root.right, path + str(root.val) + "->", res)

    
        
# @lc code=end

