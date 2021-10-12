#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        cache = set()
        while n not in cache:
            cache.add(n)
            n = sum([int(x) ** 2 for x in str(n)])

        return n == 1

# @lc code=end

