#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmapS = self.makeHashmap(s)
        hashmapT = self.makeHashmap(t)
        for (valueS, valueT) in zip(hashmapS.values(), hashmapT.values()):
            if valueS != valueT: return False

        return True

    def makeHashmap(self, str: str) -> dict[str, int]:
        hashmap = {}
        for i in range(len(str)):
            if str[i] in hashmap: hashmap[str[i]] += i
            else: hashmap[str[i]] = i
        
        return hashmap
# @lc code=end

