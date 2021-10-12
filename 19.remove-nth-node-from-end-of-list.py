#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        length = 0
        while node:
            length += 1
            node = node.next
        length -= n
        dummy = ListNode()
        dummy.next = head
        node = dummy
        while length > 0:
            length -= 1
            node = node.next
        node.next = node.next.next
        
        return dummy.next

# @lc code=end

