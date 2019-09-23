def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    if head==None:
        return None
    t=0
    p=head
    while t<n:
        p=p.next
        t=t+1
    if p==None:
        p=head.next
        head.next=None
        return p
    q=head
    preq=head



    while p!=None:
        p=p.next
        preq = q
        q=q.next
    preq.next=q.next
    q.next=None
    return head






