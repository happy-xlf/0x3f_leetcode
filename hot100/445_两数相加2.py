#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :445_两数相加2.py
# @Time      :2024/06/28 19:59:38
# @Author    :Lifeng
# @Description :

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
        l3 = self.addtwo(l1,l2)
        return self.reverseList(l3)
    def reverseList(self,head):
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre =cur
            cur = nxt
        return pre
    
    def addtwo(self, l1, l2):
        cur = dummy = ListNode()
        carry = 0
        while l1 or l2 or carry:
            if l1: carry += l1.val
            if l2: carry += l2.val
            cur.next = ListNode(carry%10)
            carry //= 10
            cur = cur.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return dummy.next
