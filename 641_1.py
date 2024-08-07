#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/5 13:13
# @Author  : sunaolin
# @File    : 641_1.py

class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.data=[0]*(k+1)
        self.head=0
        self.rear=0
        self.cap=k+1



    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.data[self.head]=value
        self.head=(self.head+1)%self.cap
        return True



    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.rear=(self.rear-1)%self.cap
        self.data[self.rear]=value
        return True


    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.head=(self.head-1)%self.cap
        return True


    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.rear=(self.rear+1)%self.cap
        return True


    def getFront(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.data[(self.head-1)%self.cap]


    def getRear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.data[self.rear]


    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.head==self.rear


    def isFull(self):
        """
        :rtype: bool
        """
        if (self.head+1)%self.cap==self.rear:
            return True
        return False



# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()