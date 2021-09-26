#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        stack = []
        for c in s:
            if c in parentheses: 
                if stack != [] and parentheses[c] == stack.pop(): continue
                else: return False
                
            stack.append(c)
        
        return stack == []


# @lc code=end

