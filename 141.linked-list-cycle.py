#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        try:
            walker = head
            runner = head.next
            while walker is not runner:
                walker = walker.next
                runner = runner.next.next
            
            return True
        except:
            return False
# @lc code=end

