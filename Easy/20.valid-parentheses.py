#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#


# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        brackets: dict = {")": "(", "}": "{", "]": "["}
        stack: list = []

        for char in s:
            if char in brackets:
                top_element = stack.pop() if stack else "#"

                if brackets[char] != top_element:
                    return False

            else:
                stack.append(char)

        return not stack


# @lc code=end
