#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :面试题_链表求和.py
# @Time      :2024/07/14 17:39:19
# @Author    :Lifeng
# @Description : https://leetcode.cn/problems/sum-lists-lcci/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        cur = head
        extar_add = 0
        sum = 0
        while l1 or l2 or extar_add!=0:
            if l1 != None:
                sum += l1.val
                l1 = l1.next
            if l2 != None:
                sum += l2.val
                l2 = l2.next
            if extar_add != 0:
                sum += extar_add
            
            cur.next = ListNode(sum % 10)
            extar_add = sum // 10
            sum = 0
            cur = cur.next
        
        return head.next



if __name__ == "__main__":
    s = Solution()

    l1 = ListNode(2)    
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    ans = s.addTwoNumbers(l1, l2)

    while ans != None:
        print(ans.val)
        ans = ans.next