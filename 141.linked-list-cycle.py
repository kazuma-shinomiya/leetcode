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
        if not head: return False

        walker = head
        runner = head

        while runner.next and runner.next.next:
            walker = walker.next
            runner = runner.next.next
            if walker == runner: return True
        
        return False
# @lc code=end

