#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/7 15:37
# @Author  : sunaolin
# @File    : 672_1.py


class Solution(object):
    def flipLights(self, n, presses):
        """
        :type n: int
        :type presses: int
        :rtype: int
        """
        ##每类操作数量如果是2的倍数，都可以当做无操作
        ##每类操作化简成0和1，状态为[0,0,0,0]四位表示，
        ##如果press为奇数，则状态中1的个数为奇数，如果为偶数，状态中1的个数为0或者偶数
        ##开关2和3的两次操作等于一次开关1的一次操作

        ##presses次数如果为偶数且大于5

        if presses%2==0:
            presses=min(presses,4)
        else:
            presses=min(presses,5)
        print(presses)

        stat=[0,0,0,0]
        res=[]
        self.dfs(stat,presses,res)
        print(res)
        vis=set()
        for v in res:
            tmp=[False]*n
            if v[0]==1:
                for i in range(n):
                    tmp[i]=not tmp[i]
            if v[1] == 1:
                for i in range(n):
                    if i%2==1:
                        tmp[i] = not tmp[i]
            if v[2] == 1:
                for i in range(n):
                    if i%2==0:
                        tmp[i] = not tmp[i]
            if v[3] == 1:
                for i in range(n):
                    if  (i+1-1)%3==0:
                        tmp[i] = not tmp[i]

            if tuple(tmp) not in vis:
                vis.add(tuple(tmp))
        # print(vis)
        return len(vis)







    def dfs(self,stat,press,res):
        if press==0:
            print(stat)
            if stat[1]==1 and stat[2]==1:
                stat[1]=0
                stat[2]=0
                stat[0]+=1
                stat[0]%=2

            if tuple(stat) not in res:
                res.append(tuple(stat))
            return

        if press>0:
            for i in range(len(stat)):
                newstat=stat[:]
                newstat[i]+=1
                newstat[i]%=2
                self.dfs(newstat,press-1,res)



a=Solution()
n=1
p=1
print(a.flipLights(n,p))

