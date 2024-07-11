#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   142_环形链表2.py
@Time    :   2024/03/27 16:37:33
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # low : a+b
        # fast: a+b+n(b+c)
        # a+b+n(b+c) = 2(a+b) => a-c = n(b+c)
        # 证明从相遇的地方，走c步就到环形链表的头节点，链表头节点走c步也到环形链表的头节点
        low = fast = head
        while fast and fast.next:
            low = low.next
            fast = fast.next.next
            if low == fast:
                while head != low:
                    head = head.next
                    low = low.next
                return low
        return None