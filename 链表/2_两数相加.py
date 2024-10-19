#!/usr/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   2_两数相加.py
@Time    :   2024/10/16 15:18:11
@Author  :   Lifeng Xu 
@desc :   
'''
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(root):
            pre = None
            while root:
                nxt = root.next
                root.next = pre
                pre = root
                root = nxt
            return pre
        l1_re = l1
        l2_re = l2
        
        k = 0
        pre = None
        while l1_re or l2_re or k:
            if l1_re and l2_re:
                s = l1_re.val + l2_re.val + k
                l1_re = l1_re.next
                l2_re = l2_re.next
            elif l1_re:
                s = l1_re.val + k
                l1_re = l1_re.next
            elif l2_re:
                s = l2_re.val + k
                l2_re = l2_re.next
            else:
                s = k
            value = s%10
            k = s//10
            node = ListNode(value)
            node.next = pre
            pre = node
        ans = reverse(pre)
        return ans
            