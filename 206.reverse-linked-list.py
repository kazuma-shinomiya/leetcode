#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None

        stack = []
        node = head
        while node:
            stack.append(node.val)
            node = node.next
        result = ListNode(stack.pop())
        node = result
        while stack != []:
            node.next = ListNode(stack.pop())
            node = node.next

        return result

# @lc code=end

