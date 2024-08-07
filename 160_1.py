#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/2 20:21
# @Author  : sunaolin
# @File    : 160_1.py

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


######重点关注
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        la=0
        p=headA
        while p:
            la+=1
            p=p.next
        lb=0
        p=headB
        while p:
            lb+=1
            p=p.next

        if la<lb:
            p=headB
            q=headA

        else:
            p=headA
            q=headB
        # i=1   这种写法默认是i=1开始统计，会忽略
        # while i<abs(la-lb):
        #     p=p.next
        #     i+=1

        i=0
        while i<abs(la-lb):
            i+=1
            p=p.next


        while p!=q:
            p=p.next
            q=q.next
        return p
