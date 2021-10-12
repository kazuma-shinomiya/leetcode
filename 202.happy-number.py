#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        cache = {}
        while n != 1:
            if n in cache: return False

            cache[n] = 1
            result = 0
            while n > 0:
                result += pow(n % 10, 2)
                n //= 10
            n = result

        return True

# @lc code=end

