# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        ######思路错了 p-q-r 换的应该是q,r的指针，而不是p,q的指针
        dummyhead=ListNode(0)
        dummyhead.next=head
        r = dummyhead

        p=head
        if head!=None:
            q=head.next
        else:
            return None

        while p!=None and q!=None:
            p.next=q.next
            q.next=p
            r.next=q
            r=p
            p=r.next
            if p!=None:
                q=p.next


        return dummyhead.next



