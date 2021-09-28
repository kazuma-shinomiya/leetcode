#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        finalMax = nums[0]
        currentMax = nums[0]
        for i in range(1, len(nums)):
            currentMax = max(currentMax + nums[i] ,nums[i])
            finalMax = max(currentMax ,finalMax)
        
        return finalMax
# @lc code=end

