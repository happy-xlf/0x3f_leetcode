#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   25_K 个一组翻转链表.py
@Time    :   2024/03/27 16:04:47
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
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        tmp = head
        cnt = 0
        while tmp:
            tmp = tmp.next
            cnt += 1
        p0 = dumyNode = ListNode(next=head)
        pre = None
        cur = head
        while cnt >= k:
            cnt -= k
            for _ in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            
            nxt = p0.next
            nxt.next = cur
            p0.next = pre
            p0 = nxt
        return dumyNode.next
            
                

        