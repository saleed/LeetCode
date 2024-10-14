#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/9/18 17:17
# @Author  : sunaolin
# @File    : 23_3.py

import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        ptrs=[]
        dum=ListNode(0)
        r=dum
        for v in lists:
            ptrs.append((v[0].val,v[0]))
        heapq.heapify(ptrs)
        while len(ptrs)>0:
            top=heapq.heappop(ptrs)
            if top.next:
                heapq.heappush((top.next.val,top.next))
            top.next=None
            r.next=top
        return dum.next






