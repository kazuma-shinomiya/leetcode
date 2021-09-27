#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        iterator1 = l1
        iterator2 = l2
        result = iteratorR = ListNode()
        while iterator1 and iterator2:
            if iterator1.val <= iterator2.val:
                iteratorR.next = iterator1
                iterator1 = iterator1.next
            else:
                iteratorR.next = iterator2
                iterator2 = iterator2.next
            
            iteratorR = iteratorR.next
        
        iteratorR.next = iterator1 or iterator2

        return result.next
# @lc code=end

