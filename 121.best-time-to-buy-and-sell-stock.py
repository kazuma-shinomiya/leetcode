#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = sys.maxsize
        maxPrice = 0
        for price in prices:
            minPrice = min(price, minPrice)
            maxPrice = max(price - minPrice, maxPrice)
        
        return maxPrice

# @lc code=end

