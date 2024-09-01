    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    # @Time    : 2024/8/14 17:23
    # @Author  : sunaolin
    # @File    : 725_1.py


    # Definition for singly-linked list.
    # class ListNode(object):
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
    class Solution(object):
        def splitListToParts(self, head, k):
            """
            :type head: ListNode
            :type k: int
            :rtype: List[ListNode]
            """

            l=0
            p=head
            while p:
                l+=1
                p=p.next
            if k>l:
                k=l

            larr=[int(l/k)]*k
            left=l%k
            for i in range(left):
                larr[i]+=1

            dum=ListNode(0)
            p=dum
            res=[]
            res.append(head)
            for i in range(len(larr)):
                cnt=0
                while cnt<larr[i] and p.next:
                    cnt+=1
                    p=p.next

                q=p.next
                p.next=None
                p=q

                res.append(q)
                if p==None:
                    break

            res+=[]*(k-l)
            return res



