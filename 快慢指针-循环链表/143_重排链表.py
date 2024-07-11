#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   143_重排链表.py
@Time    :   2024/03/27 16:45:45
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
    # node mid
    def mid_ListNode(self, node):
        low = fast = node
        while fast and fast.next:
            low = low.next
            fast = fast.next.next
        return low
        
    def reverse(self, head):
        p0 = dumpy = ListNode(next=head)
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur =nxt
        return p0.next
    
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        mid = self.mid_ListNode(head)
        mid = self.reverse(mid)
        p0 = ListNode(next=head)
        cur = head
        while mid:
            nxt = cur.next
            mxt = mid.next  
            cur.next = mid
            mid.next = nxt

            cur = nxt
            mid = mxt
        return p0.next