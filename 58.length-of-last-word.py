#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = []
        word = ''
        for c in s:
            if c == ' ': 
                if word == '': continue
                words.append(word)
                word = ''
            else: word += c
        if word != '': words.append(word)
        
        return len(words[-1]) 

# @lc code=end

