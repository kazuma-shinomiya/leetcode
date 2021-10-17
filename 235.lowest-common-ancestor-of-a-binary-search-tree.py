#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self) -> None:
        self.answer = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recurseTree(current):
            if not current: return False

            left = recurseTree(current.left)
            right = recurseTree(current.right)
            middle = current == p or current == q
            if middle + left + right >= 2:
                self.answer = current
            
            return middle or left or right
        
        recurseTree(root)
        return self.answer
# @lc code=end

