#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: ListNode | None, list2: ListNode | None
    ) -> ListNode | None:
        merged: ListNode = None
        sorted: ListNode = None

        while list1 or list2:
            if not list1 and list2:
                while list2:
                    merged = ListNode(list2.val, merged)
                    list2 = list2.next

                break

            elif not list2 and list1:
                while list1:
                    merged = ListNode(list1.val, merged)
                    list1 = list1.next

                break

            if list1.val >= list2.val:
                merged = ListNode(list2.val, merged)
                list2 = list2.next

            elif list1.val < list2.val:
                merged = ListNode(list1.val, merged)
                list1 = list1.next

        while merged:
            sorted = ListNode(merged.val, sorted)
            merged = merged.next

        return sorted


# @lc code=end
