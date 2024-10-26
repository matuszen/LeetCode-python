#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        valid: bool = False
        pref: str = strs[0]
        
        while not valid:
            for word in strs[1:]:
                if not word.startswith(pref):
                    pref = pref[:-1]
                    break
            
            else:
                valid = True
        
        return pref

# @lc code=end
