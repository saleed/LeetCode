#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/9/1 17:35
# @Author  : sunaolin
# @File    : 855.py


class ExamRoom(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.interval=[]
        self.n=n
        self.cnt=0



    def seat(self):
        """
        :rtype: int
        """
        self.cnt += 1
        if self.cnt==1:
            return 0
        if self.cnt==2:
            self.interval=[[0,self.n-1]]
            return self.n-1
        maxitv=0
        id=-1
        for i in range(len(self.interval)):
            v=self.interval[i]
            if maxitv<v[1]-v[0]:
                maxitv=v[1]-v[0]
                id=i
        sp=self.interval[id]
        self.interval=self.interval[:id]+[[sp[0],(sp[0]+sp[1])/2-1],[(sp[0]+sp[1])/2+1,sp[1]]]+self.interval[id+1:]
        return (sp[0]+sp[1])/2







    def leave(self, p):
        """
        :type p: int
        :rtype: None
        """
        id=-1
        if p==self.interval[0]-1:
            self.interval[0]=[p,self.interval[0][1]]
            return
        for i in range(len(self.interval)):
            v=self.interval[i]
            if v[1]+1==p:
                id=i
                break
        self.




# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)