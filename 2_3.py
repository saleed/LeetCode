# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #不做结构变换，直接按照加法规则处理

        p=l1
        q=l2
        c=0
        newhead=ListNode(0)
        ptr=newhead
        while p!=None or q!=None:
            if p==None:
               add1=0
            else:
               add1=p.val
               p=p.next
            if q==None:
               add2=0
            else:
               add2=q.val
               q=q.next
            new=ListNode((add1+add2+c)%10)
            c=(add1+add2+c)/10
            ptr.next=new
            ptr=ptr.next
        if c:
            ptr.next=ListNode(1)
        return newhead.next







test=[1,2,[1,23]]

print(test[2])







