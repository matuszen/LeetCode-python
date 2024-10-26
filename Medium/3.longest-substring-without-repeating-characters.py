#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#


# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subs: list[set[str]] = []

        for i in range(len(s)):
            subs.append({s[i]})

            for j in range(i + 1, len(s)):
                if s[j] not in subs[i]:
                    subs[i].add(s[j])

                else:
                    break

        return max(map(len, subs)) if subs else 0


# @lc code=end
