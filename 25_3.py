#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/16 14:31
# @Author  : sunaolin
# @File    : 25_3.py

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
        dum=ListNode(0)
        dum.next=head
        preHead=dum
        while True:
            p=preHead.next
            n=0
            while p and n<k-1:
                n+=1
                p=p.next  ####n=k后，p指向了下一个节点！！！
            if n!=k-1 or p==None:  #######注意这里的边界条件，有可能为空，为空的时候说明没有取到长度为k的子序列
                return dum.next
            tailNext=p.next
            p.next=None ###注意这里，如果不置空，翻转会出错
            head,tail=self.reverse(preHead.next,p)
            # print(head)
            # print(tail)
            # print(tailNext)

            preHead.next=head
            tail.next=tailNext
            preHead=tail
            # print(dum)




    def reverse(self,head,tail):
        p=head
        q=p.next if p else None
        r=q.next if q else None
        p.next=None
        while q:  ####这里有问题，注意能这样判断一定且必定tail.next为空 或者合理改为q!=tail
            q.next=p
            p=q
            q=r
            r=r.next if r else None
        return tail ,head

