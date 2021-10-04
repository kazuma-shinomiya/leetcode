#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = {}
        for num in nums:
            if num in hashmap: hashmap.pop(num)
            else: hashmap[num] = num
        
        return list(hashmap.keys())[0]
# @lc code=end

