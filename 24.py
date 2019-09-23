# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None





class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return head

        p=head
        newhead=head.next
        q=p.next
        while p!=None and q!=None:
            r=q.next
            if r!=None:
                s=r.next
            else:
                s=None
            q.next=p
            if s!=None:
                p.next=s
            elif r!=None:
                p.next=r
            else:
                p.next=None
            p=r
            q=s
        return newhead


# 最优思路
# 和链表反转类似，关键在于　有三个指针，分别指向前后和当前节点。不同点是两两交换后，移动节点步长为２

