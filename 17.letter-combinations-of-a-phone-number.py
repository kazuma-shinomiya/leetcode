#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
from collections import deque

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        results = deque()
        if digits == "": return results
        alphabet = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        results.append("")
        while len(results[0]) != len(digits):
            current = results.popleft()
            map = alphabet[digits[len(current)]]
            for c in map:
                results.append(current + c)
        
        return results
# @lc code=end

