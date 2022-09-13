# 21. Merge Two Sorted Lists
# You are given the heads of two sorted linked lists list1 and list2. Merge the two lists in a one sorted list.\
# The list should be made by splicing together the nodes of the first two lists. Return the head of the merged linked
# list.
#
# Example 1:
# Input: list1 = [1, 2, 4], list2 = [1, 3, 4]
# Output: [1, 1, 2, 3, 4, 4]
#
# Example 2:
# Input: list1 = [], list2 = []
# Output: []
#
# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    list2 += list1

    list2 = sorted(list2, key=list2.val)

    pass


list1_data = [1, 2, 4]
list2_data = [1, 3, 4]
# Output [1,1,2,3,4,4]

mergeTwoLists(list1_data, list2_data)
