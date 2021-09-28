#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentMaxes = [0] * len(nums)
        currentMaxes[0] = nums[0]
        result = currentMaxes[0]
        for i in range(1, len(nums)):
            currentMaxes[i] = nums[i] + (currentMaxes[i-1] if currentMaxes[i-1] > 0 else 0)
            result = max(currentMaxes[i] ,result)
        
        return result
# @lc code=end

