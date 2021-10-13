#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        def backtrack(result = [], left = 0, right = 0):
            if len(result) == n * 2:
                results.append("".join(result))
                return
            if left < n:
                result.append("(")
                backtrack(result, left+1, right)
                result.pop()
            if right < left:
                result.append(")")
                backtrack(result, left, right+1)
                result.pop()
        backtrack()
        return results

# @lc code=end

