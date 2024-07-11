# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        pre = None
        cur = slow if fast == None else slow.next
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        while pre and head:
            if pre.val != head.val:
                return False
            pre = pre.next
            head = head.next
        return True
