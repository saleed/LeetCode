# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p=head
        count=0
        pre_p=ListNode(0)
        pre_p.next=head
        q=pre_p

        while count<n and p!=None:
            p=p.next
            count+=1

        ##大坑，一定是count<n时候才直接return

        # [1]
        # 1
        # 输出：
        # [1]
        # 预期结果：
        # []
        if p==None and count<n:
            return head

        while p!=None:
            p=p.next
            q=q.next
        rmv=q.next
        q.next=rmv.next
        rmv.next = None
        return pre_p.next





