#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#


# @lc code=start
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        return [
            int(number)
            for number in str(int("".join([str(digit) for digit in digits])) + 1)
        ]


# @lc code=end
