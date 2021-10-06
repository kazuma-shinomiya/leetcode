#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        maxWater = 0
        while start < end:
            water = (end-start) * min(height[start], height[end])
            maxWater = max(water, maxWater)
            if height[start] < height[end]: start += 1
            else: end -= 1
        
        return maxWater
# @lc code=end

