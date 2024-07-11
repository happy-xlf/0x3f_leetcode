#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   206_反转链表.py
@Time    :   2024/03/25 14:35:40
@Author  :   Lifeng
@Version :   1.0
@Desc    :   None
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        now = head
        while now:
            next = now.next
            now.next = pre
            pre = now
            now = next
        return pre
        

