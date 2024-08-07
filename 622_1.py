#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/3 13:51
# @Author  : sunaolin
# @File    : 622_1.py


class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """

        ##环形队列中一定要空出来一个位置，否则队列为空和满无法判断
        self.que=[0]*(k+1)
        self.rear=0
        self.head=0
        self.cap=k+1


    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if (self.rear+1)%self.cap==self.head:
            return False
        self.que[self.rear]=value
        self.rear=(self.rear+1)%self.cap
        return True


    def deQueue(self):
        """
        :rtype: bool
        """
        if self.head==self.rear:
            return False
        # ret=self.que[self.head]
        self.head=(self.head+1)%self.cap

        return True


    def Front(self):
        """
        :rtype: int
        """
        if self.rear==self.head:
            return -1
        return self.que[self.head]


    def Rear(self):
        """
        :rtype: int
        """
        if self.rear==self.head:
            return -1
        return self.que[(self.rear-1)%self.cap]

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.rear==self.head


    def isFull(self):
        """
        :rtype: bool
        """
        return (self.rear+1)%self.cap==self.head



# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()