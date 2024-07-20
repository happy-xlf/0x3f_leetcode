#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :86_分割链表.py
# @Time      :2024/07/20 15:46:09
# @Author    :Lifeng
# @Description : https://leetcode.cn/problems/partition-list/description/
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small = ListNode(0)
        p = small
        big = ListNode(0)
        q = big
        while head:
            if head.val < x:
                p.next = ListNode(head.val)
                p = p.next
            else:
                q.next = ListNode(head.val)
                q = q.next
            head = head.next
        p.next = big.next
        return small.next        


if __name__ == "__main__":
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(4)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(2)
    head = s.partition(head, 3)
    while head: print(head.val, end="->"); head = head.next