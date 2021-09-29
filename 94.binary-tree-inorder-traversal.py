#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        results = []
        if root == None: return results
        
        results = self.inorderHelper(root, results)

        return results
    
    def inorderHelper(self, root: Optional[TreeNode], array: List[int]) -> List[int]:
        if root == None: return None

        self.inorderHelper(root.left, array)
        array.append(root.val)
        self.inorderHelper(root.right, array)

        return array
# @lc code=end

