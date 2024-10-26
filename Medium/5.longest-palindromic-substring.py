#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#


# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""

        start, max_length = 0, 1

        for i in range(1, len(s)):
            low, high = i - 1, i

            while low >= 0 and high < len(s) and s[low] == s[high]:
                if high - low + 1 > max_length:
                    start = low
                    max_length = high - low + 1
                low -= 1
                high += 1

            low, high = i - 1, i + 1

            while low >= 0 and high < len(s) and s[low] == s[high]:
                if high - low + 1 > max_length:
                    start = low
                    max_length = high - low + 1
                low -= 1
                high += 1

        return s[start : start + max_length]


# @lc code=end
