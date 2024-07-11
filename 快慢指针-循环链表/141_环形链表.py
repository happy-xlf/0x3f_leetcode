#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   141_环形链表.py
@Time    :   2024/03/27 16:34:00
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        low = fast = head
        while fast and fast.next:
            low = low.next
            fast = fast.next.next
            if low == fast:
                return True
        return False
        