# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#合并两个有序链表

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        p=list1
        q=list2
        head=ListNode(0)
        tmp=head
        while p and q:
            if p.val<q.val:
                tmp.next=p
                p=p.next
            else:
                tmp.next=q
                q=q.next
            tmp=tmp.next
        if p:
            tmp.next=p
        if q:
            tmp.next=q
        return head.next
        