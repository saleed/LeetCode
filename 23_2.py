#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/16 11:44
# @Author  : sunaolin
# @File    : 23_2.py

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        return self.multiCombineWithHeap(lists)



    ###多路归并，超时
    def mulitiCombine(self,lists):
        if len(lists)==0:
            return None
        newhead=ListNode(0)
        r=newhead
        # print(type(lists),type(lists[0]))

        plist=[None]*len(lists)
        print(plist,type(plist))
        for i in range(len(lists)):
            plist[i]=lists[i] if lists[i] is not None else None
        # print(plist)
        while True:
            minv=float("inf")
            sid=-1
            for i in range(len(plist)):
                tmpv=plist[i].val if plist[i] else float("inf")
                if tmpv<minv:
                    minv=plist[i].val
                    sid=i
            if sid!=-1:
                print(sid)
                q=plist[sid]
                plist[sid]=q.next
                r.next=q
                q.next=None
                r=r.next
            else:
                # print(type(newhead.next))
                return newhead.next

    ##使用堆优化
    def multiCombineWithHeap(self,lists):
        if len(lists) == 0:
            return None
        newhead = ListNode(0)
        r = newhead
        # print(type(lists),type(lists[0]))
        plist=[]
        for i in range(len(lists)):
            if lists[i] is not None:
                plist.append((lists[i].val,lists[i]))
        heapq.heapify(plist)
        # print("###",plist)
        while len(plist)>0:
            pop=heapq.heappop(plist)
            q = pop[1].next
            r.next=pop[1]
            pop[1].next=None
            r=r.next
            if q:
                heapq.heappush(plist,(q.val,q))
        return newhead.next

##堆测试
import  heapq
test=[3,4,6,8,9,0]
heapq.heapify(test)
print(test)
# [0, 4, 3, 8, 9, 6]
# 使用数组构造了堆
test=[(2,2),(8,4),(6,8),(9,0),(0,3)]
heapq.heapify(test)
print(test)
# (0, 3), (2, 2), (6, 8), (9, 0), (8, 4)]
# 默认按照首字母排序
print(heapq.heappushpop(test,(-1,0)))


