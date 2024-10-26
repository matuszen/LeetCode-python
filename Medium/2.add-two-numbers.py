#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        s1: str = ""
        s2: str = ""

        while l1 or l2:
            if l1 and l2:
                s1 += str(l1.val)
                s2 += str(l2.val)
                l1 = l1.next
                l2 = l2.next

            elif l1 and not l2:
                s1 += str(l1.val)
                l1 = l1.next

            elif l2 and not l1:
                s2 += str(l2.val)
                l2 = l2.next

        result: str = str(int(s1[::-1]) + int(s2[::-1]))
        resultList: ListNode = None

        for digit in result:
            resultList = ListNode(int(digit), resultList)

        return resultList


# @lc code=end
