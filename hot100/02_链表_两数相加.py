# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        t=0
        root=ListNode()
        p=root
        while l1 and l2:
            x1=l1.val
            x2=l2.val
            s=(x1+x2+t)%10
            t=(x1+x2+t)//10
            newnode=ListNode(s)
            p.next=newnode
            p=p.next
            l1=l1.next
            l2=l2.next
        
        while l1:
            x1=l1.val
            s=(x1+t)%10
            t=(x1+t)/10
            newnode=ListNode(s)
            p.next=newnode
            p=p.next
            l1=l1.next

        while l2:
            x2=l2.val
            s=(x2+t)%10
            t=(x2+t)/10
            newnode=ListNode(s)
            p.next=newnode
            p=p.next
            l2=l2.next
        
        if t!=0:
            newnode=ListNode(int(t))
            p.next=newnode

        return root.next

if __name__ == '__main__':
    l1=ListNode()
    newNode=ListNode(9)
    newNode2=ListNode(9)
    newNode3=ListNode(9)

    l1.next=newNode
    newNode.next=newNode2
    newNode2.next=newNode3

    l2=ListNode()
    newNode4=ListNode(9)
    newNode5=ListNode(9)


    l2.next=newNode4
    newNode4.next=newNode5

    l1=l1.next
    l2=l2.next

    s=Solution()
    ans=s.addTwoNumbers(l1,l2)

    while ans:
        print(ans.val)
        ans=ans.next
    

    #写一个二分排序

    







