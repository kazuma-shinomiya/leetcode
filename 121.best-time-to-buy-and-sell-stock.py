#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = [sys.maxsize]
        maxPrice = 0
        for price in prices:
            if price <= stack[-1]: 
                stack.append(price)
                continue

            maxPrice = max(price - stack[-1], maxPrice)
        
        return maxPrice

# @lc code=end
