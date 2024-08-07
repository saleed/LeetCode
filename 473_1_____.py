#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/24 13:45
# @Author  : sunaolin
# @File    : 473_1.py


class Solution(object):
    def makesquare(self, matchsticks):
        """
        :type matchsticks: List[int]
        :rtype: bool
        """
        if sum(matchsticks)%4!=0:
            return False
        for v in matchsticks:
            if v>sum(matchsticks)/4:
                return False
        vis=[0 for _ in range(len(matchsticks))]
        matchsticks.sort()
        matchsticks=matchsticks[::-1]
        print(matchsticks)
        return self.dfs(matchsticks,vis,0,sum(matchsticks)/4,0)

    def dfs(self,mset,vis,mnum,target,tmpl):
        print(mset,tmpl)
        if mnum==4:
            return True


        for i in range(len(vis)):
            if vis[i]==1:
                continue
            else:
                if tmpl+mset[i]>target:
                    continue
                vis[i]=1
                if tmpl+mset[i]==target:
                    self.dfs(mset,vis,mnum+1,target,0):
                        return True
                else:
                    if self.dfs(mset,vis,mnum,target,tmpl+mset[i]):
                        return True
                vis[i]=0    ###一定要注意状态还原
        return False


matchsticks =[5,5,5,5,16,4,4,4,4,4,3,3,3,3,4]
a=Solution()
print(sum(matchsticks)/4)
print(a.makesquare(matchsticks))