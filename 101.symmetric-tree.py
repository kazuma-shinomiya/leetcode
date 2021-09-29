#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and root.right: return False
        if root.left and not root.right: return False

        return self.helper(root.left, root.right)

    def helper(self, leftT: Optional[TreeNode], rightT: Optional[TreeNode]) -> bool:
        if leftT and rightT:
            return leftT.val == rightT.val and self.helper(leftT.left, rightT.right) and self.helper(leftT.right, rightT.left)
            
        return leftT is rightT

# @lc code=end

