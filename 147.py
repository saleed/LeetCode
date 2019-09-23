
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return head
        dummy=ListNode(0)
        sortlist=dummy
        newhead=ListNode(0)
        newhead.next=head
        p=newhead
        while p.next!=None:
            q=p.next
            p.next=p.next.next
            q.next=None
            if sortlist.next==None:
                sortlist.next=q
            else:
                flag=0
                while sortlist.next!=None:
                    if sortlist.next.val>q.val:
                        q.next=sortlist.next
                        sortlist.next=q
                        flag=1
                        break
                    sortlist=sortlist.next
                if flag==0:
                    sortlist.next=q
                sortlist=dummy
        return dummy.next


