# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        i = 0
        a = 0
        while l1:
            a += (10 ** i) * l1.val
            i += 1
            l1 = l1.next

        i = 0
        b = 0
        while l2:
            b += (10 ** i) * l2.val
            i += 1
            l2 = l2.next

        c = list(map(int, list(reversed(str(a + b)))))
        node_list = [ListNode(x, None) for x in c]
        for i in range(len(node_list) - 1):
            node_list[i].next = node_list[i + 1]
        return node_list[0]


if __name__ == "__main__":
    s = Solution()
    a = ListNode(2, ListNode(4, ListNode(3, None)))
    b = ListNode(5, ListNode(6, ListNode(4, None)))
    print(s.addTwoNumbers(a, b))
