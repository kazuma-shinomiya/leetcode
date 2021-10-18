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

        fast = head.next
        slow = head
        result = ListNode()
        node = result
        while fast and fast.next:
            print(fast.val, slow.val)
            node.next = ListNode(fast.val)
            node = node.next
            node.next = ListNode(slow.val)
            node = node.next
            fast = fast.next.next
            slow = slow.next.next
        
        if fast:
            node.next = ListNode(fast.val)
            node = node.next
            node.next = ListNode(slow.val)
            node = node.next
        elif slow:
            node.next = ListNode(slow.val)

        return result.next

# @lc code=end

