#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1]
        for i in range(rowIndex):
            result = list(map(lambda x, y: x + y, result + [0], [0] + result))
            
        return result
# @lc code=end

