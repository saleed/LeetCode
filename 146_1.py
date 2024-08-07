#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/1 20:13
# @Author  : sunaolin
# @File    : 146——1.py

class biNode:
    def __init__(self,k,val):
        self.val=(k,val)
        self.pre=None
        self.next=None



class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head=biNode(0,0)
        self.tail=biNode(0,0)
        self.head.next=self.tail
        self.tail.pre=self.head
        self.cap=capacity

        self.data={}



    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.data:
            pre = self.data[key].pre
            next = self.data[key].next

            tmp=self.data[key]
            tmp.next=None
            tmp.pre=None

            pre.next=next
            next.pre=pre

            q=self.head.next
            self.head.next=tmp
            tmp.pre=self.head
            tmp.next=q
            q.pre=tmp

            return self.data[key].val[1]

        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.data:
            self.data[key].val=(key,value)
            self.get(key)
            return

        elif len(self.data)==self.cap:
            pre=self.tail.pre
            ppre=pre.pre
            ppre.next=self.tail
            self.tail.pre=ppre

            pre.pre=None
            pre.next=None
            del self.data[pre.val[0]]

        next=self.head.next
        tmp=biNode(key,value)
        tmp.pre=self.head
        tmp.next=next
        self.head.next=tmp
        next.pre=tmp
        self.data[key]=tmp
        return


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)