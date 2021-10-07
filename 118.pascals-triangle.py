#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        results = []
        for i in range(1, numRows + 1):
            addedRow = []
            addedRow.append(1)
            if i == 1: 
                results.append(addedRow)
                continue

            if i >= 3: 
                for j in range(i - 2):
                    addedRow.append(results[-1][j] + results[-1][j + 1])
            addedRow.append(1)
            results.append(addedRow)

        return results
# @lc code=end

