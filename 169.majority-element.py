#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}

        for num in nums:
            if num in hashmap: hashmap[num] += 1
            else: hashmap[num] = 1
        
        maxCount = 0
        result = 0
        for num, count in hashmap.items():
            if count > maxCount: 
                maxCount = count
                result = num
        
        return result

# @lc code=end

