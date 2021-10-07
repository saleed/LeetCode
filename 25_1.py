# coding:utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummyHead = ListNode(head)
        dummyHead.next = head

        total_len = 0
        p = dummyHead
        while p.next != None:
            total_len += 1
            p = p.next
        p = dummyHead

        for i in range(total_len / k):
            p = self.reverseList(p, k)
            count = 0
            while count < k:
                p = p.next
                count += 1

        return dummyHead.next

    # 这里startNode定义为翻转段的前一个节点
    def reverseList(self, startNode, k):
        p = startNode.next
        if p == None:
            return
        q = p.next
        if q == None:
            return
        r = q.next
        count = 0
        while count < k - 1:
            q.next = p
            p = q
            q = r
            if r != None:
                r = r.next
            count += 1
        tail = startNode.next
        startNode.next = q
        tail.next = r
        # print(startNode)
        return