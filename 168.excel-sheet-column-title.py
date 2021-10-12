#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alphabetInitial = ord("A")
        result = []
        while columnNumber > 0:
            alphabetCode = (columnNumber-1) % 26
            result.append(chr(alphabetCode + alphabetInitial))
            columnNumber = (columnNumber-1) // 26
            
        return ''.join(reversed(result))
        
# @lc code=end

