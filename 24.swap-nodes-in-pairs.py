#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        dummy = ListNode(-1)
        dummy.next = head
        node = dummy
        while head and head.next:
            first = head
            second = head.next
            
            node.next = second
            first.next = second.next
            second.next = first

            node = first
            head = first.next

        return dummy.next

# @lc code=end

