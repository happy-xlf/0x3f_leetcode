#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   876_链表的中间结点.py
@Time    :   2024/03/27 16:30:02
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 返回中间的链表结点：快慢指针
        # 奇数：1-2-3
        low = fast = head
        while fast and fast.next:
            low = low.next
            fast = fast.next.next
        return low