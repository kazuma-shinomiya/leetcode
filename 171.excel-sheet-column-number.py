#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        alphabetInitial = 64
        results = []
        for c in columnTitle:
            results.append(ord(c) - alphabetInitial)
        
        index = len(results) - 1
        result = 0
        for number in results:
            if index > 0: result += pow(26, index) * number
            else: result += number
            index -= 1

        return result
# @lc code=end

