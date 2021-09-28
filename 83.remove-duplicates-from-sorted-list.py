#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: return head
        
        queue = []
        iterator = head
        queue.append(iterator.val)
        result = ListNode(iterator.val)
        iteratorR = result
        iterator = iterator.next
        while iterator != None:
            if iterator.val != queue[-1]: 
                queue.append(iterator.val)
                iteratorR.next = ListNode(iterator.val)
                iteratorR = iteratorR.next
            iterator = iterator.next
        
        return result

# @lc code=end

