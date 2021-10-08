#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        result = self.postorder(root, result)

        return result
    def postorder(self, root: Optional[TreeNode], array: List[int]) -> List[int]:
        if root:
            self.postorder(root.left, array)
            self.postorder(root.right, array)
            array.append(root.val)

        return array
# @lc code=end

