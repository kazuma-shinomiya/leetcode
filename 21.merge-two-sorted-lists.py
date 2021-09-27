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
        result = ListNode()
        iteratorR = result
        while iterator1 != None and iterator2 != None:
            value1 = iterator1.val
            value2 = iterator2.val
            if value1 <= value2:
                iteratorR.next = ListNode(value1)
                iterator1 = iterator1.next
            else:
                iteratorR.next = ListNode(value2)
                iterator2 = iterator2.next
            
            iteratorR = iteratorR.next
        
        if iterator1 == None: iteratorR.next = iterator2
        else: iteratorR.next = iterator1

        return result.next
# @lc code=end

