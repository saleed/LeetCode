def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    p = l1
    q = l2
    head = ListNode(0)
    nxthead=head
    while p != None or q != None:
        if p == None:
            node = ListNode(q.val)
            nxthead.next = node
            nxthead=node
            q = q.next
        elif q == None:
            node = ListNode(p.val)
            nxthead.next = node
            nxthead = node
            p = p.next
        else:
            if p.val < q.val:
                node = ListNode(p.val)
                nxthead.next = node
                nxthead = node
                p = p.next
            else:
                node = ListNode(q.val)
                nxthead.next = node
                nxthead = node
                q = q.next



