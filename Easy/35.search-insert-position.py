#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#


# @lc code=start
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i, number in enumerate(nums):
            if number >= target:
                return i

        else:
            return len(nums)


# @lc code=end
