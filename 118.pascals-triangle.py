#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        results = [[1]]
        for i in range(1, numRows):
            results = results + [list(map(lambda x, y: x+y, results[-1] + [0], [0] + results[-1]))]

        return results[:numRows]
# @lc code=end

