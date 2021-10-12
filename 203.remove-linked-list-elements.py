#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        sentinel = ListNode()
        sentinel.next = head
        prev, current = sentinel, head
        while current:
            if current.val == val: prev.next = prev.next.next
            else: prev = current
            current = current.next
        
        return sentinel.next
# @lc code=end

