#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/18 14:18
# @Author  : sunaolin
# @File    : 401_1.py

class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        res=[]
        self.dfs(turnedOn,0,"",res)
        return res



    def dfs(self,num,i,tmp,res):
        if i==11 and num==0:
            time=self.decode(tmp)
            if time!="":
                res.append(time)
            return
        if i<11:
            self.dfs(num,i+1,tmp+"0",res)
            self.dfs(num-1,i+1,tmp+"1",res)

    def decode(self,tstr):
        hour=0
        minute=0
        for i in range(4)[::-1]:
            if tstr[i]=="1":
                hour+=(1<<(3-i))
        for i in range(4,11)[::-1]:
            if tstr[i]=="1":
                minute+=(1<<(10-i))
        if hour>=12 or minute>=60:
            return ""
        strMinute=""
        if minute<10:
            strMinute="0"+str(minute)
        else:
            strMinute=str(minute)
        return str(hour)+":"+strMinute






