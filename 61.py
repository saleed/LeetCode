
def rotateRight(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    if head == None or k==0 or k%getLen(head) == 0:
        return head
    left = k%getLen(head)+1
    p = head
    for i in range(left - 1):
        p = p.next
    q = p
    while p.next != None:
        p = p.next
    p.next = head
    newhead = q.next
    q.next = None
    return newhead


def getLen(head):
    p = head
    n = 0
    while p != None:
        p = p.next
        n = n + 1
    return n