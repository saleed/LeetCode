class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """

        prep=ListNode()
        prep.next=head
        cnt=0
        while cnt<left:
            cnt+=1
            prep=prep.next

        rq=head
        cnt=1
        while cnt<right:
            rq=rq.next
            cnt+=1

        rq=


        p=prep.next
        prep.next=None
        q=p.next if p!=None else None
        r=q.next if q!=None else None





