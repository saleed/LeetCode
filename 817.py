#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/27 15:00
# @Author  : sunaolin
# @File    : 817.py


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def numComponents(self, head, nums):
        """
        :type head: ListNode
        :type nums: List[int]
        :rtype: int
        """

        p=head
        stat=0
        cnt=0
        while p:
            if p.val in nums:
                if stat==0:
                    stat=1
                    cnt+=1
            else:
                stat=0
            p=p.next

        return cnt