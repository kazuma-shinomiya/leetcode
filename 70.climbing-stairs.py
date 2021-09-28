#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    cache = {
        1: 1,
        2: 2,
    }
    def climbStairs(self, n: int) -> int:
        if n in Solution.cache: return Solution.cache[n]
        else :
            result = self.climbStairs(n - 1) + self.climbStairs(n - 2)
            Solution.cache[n] = result
            
        return result
# @lc code=end

