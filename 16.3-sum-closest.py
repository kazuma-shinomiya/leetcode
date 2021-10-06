#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        result = 0
        minDiff = sys.maxsize
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]: continue

            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == target: return total

                currDiff = abs(target - total)
                if currDiff < minDiff: 
                    minDiff = currDiff
                    result = total

                if total < target: left += 1
                elif total > target: right -= 1
        
        return result
            

# @lc code=end

