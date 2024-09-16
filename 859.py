#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/9/16 18:46
# @Author  : sunaolin
# @File    : 859.py


class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        #词频不同，必然不为亲密字符；
        # 当s与goal不同的字符数量为 2（能够相互交换）」或「s 与goal不同的字符数量为0，但同时s中有出现数量超过2的字符（能够相互交换）」时，两者必然为亲密字符。



        if len(s)!=len(goal):
            return False

        id=-1
        cnt=0
        dumpNum=0
        vis=set()
        for i in range(len(s)):
            if s[i] in vis:
                dumpNum+=1
            else:
                vis.add(s[i])


            if s[i]==goal[i]:
                continue
            else:
                cnt+=1
                if id==-1:
                    id=i
                else:
                    if s[i]==goal[id] and goal[i]==s[id]:
                        id=-1
                    else:
                        return False
        if (cnt==2 and id==-1) or (cnt==0 and dumpNum>0):
            return True
        return False






