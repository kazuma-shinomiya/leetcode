#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmapS = {}
        hashmapT = {}
        for (chrS, chrT) in zip(s, t):
            if chrS not in hashmapS and chrT not in hashmapT:
                hashmapS[chrS] = chrT
                hashmapT[chrT] = chrS
            elif hashmapS.get(chrS) != chrT or hashmapT.get(chrT) != chrS:
                return False
                
        return True

# @lc code=end

