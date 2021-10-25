# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return False

        p = head
        q = head.next
        plen=1
        qlen=2
        while p != None and q != None:
            if p == q:
                break
            else:
                p = p.next
                q = q.next
                plen+=1
                qlen+=1
                if q != None:
                    q = q.next
                    qlen+=1
                else:
                    return None
        cyclelen=qlen-plen
        l=1
        ptr=head
        while ptr!=q:
            ptr=ptr.next
            l+=1
        ptr=head
        l=1
        while l<q-cyclelen:
            ptr=ptr.next
            l+=1
        return ptr











