#!/usr/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   23_合并 K 个升序链表.py
@Time    :   2024/10/17 09:37:23
@Author  :   Lifeng Xu 
@desc :   
'''
from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def merge_list(list1, list2):
            dummy = ListNode(0)
            cur = dummy
            while list1 and list2:
                if list1.val < list2.val:
                    cur.next = list1
                    list1 = list1.next
                else:
                    cur.next = list2
                    list2 = list2.next
                cur = cur.next
            if list1:
                cur.next = list1
            if list2:
                cur.next = list2
            return dummy.next
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        return merge_list(left, right)

if __name__ == '__main__':
    lists = [ListNode(1, ListNode(4, ListNode(5))), ListNode(1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))]
    s = Solution()
    ans = s.mergeKLists(lists)
    while ans:
        print(ans.val)
        ans = ans.next
        