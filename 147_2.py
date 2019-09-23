# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ####要点！！
        # 1.两层循环，一层循环遍历寻找第一个不满足有序的节点（因为涉及到删除插入，必须找无序点的前一个节点）
        # 2           二层循环在有序链中找插入点，找第一个比无序点大的节点

        # 注意操作都是找前一个节点!!!!



        dummy=ListNode(-float("inf"))
        dummy.next=head

        p=dummy
        pre=-float("inf")
        while p.next!=None:
            if p.next.val>=pre:
                pre=p.next.val
                p=p.next
                continue
            else:
                q=p.next
                p=q.next
                ptr=dummy
                while ptr.next.val<q.val:
                    ptr=ptr.next
                q.next=ptr.next
                ptr.next=q
                if p==None:
                    break
        return dummy.next

