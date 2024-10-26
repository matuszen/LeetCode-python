#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#


# @lc code=start
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        temp: set = set(nums)
        nums.clear()

        for i in temp:
            nums.append(i)

        nums.sort()

        return len(temp)


# @lc code=end
