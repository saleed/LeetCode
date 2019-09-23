# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None





#如果借助辅助内存，这个题目很简单，如果不借助辅助内存，
#遍历一遍：把大于x的节点全部连到末尾



#想复杂了，直接删除原链表中小于x的节点，插入到新链表即可。。。。。。
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy1=ListNode(0)
        dummy2=ListNode(0)
        dummy1.next=head
        p=dummy1
        q=dummy2
        while p.next!=None:
            if p.next.val<x:
                rmv=p.next
                p.next=rmv.next
                rmv.next=None
                q.next=rmv
                q=q.next
            else:
                p=p.next
        p.next=dummy1.next
        return dummy2.next





