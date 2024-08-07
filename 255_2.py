#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/9 14:32
# @Author  : sunaolin
# @File    : 255_2.py

###
class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """





    ####超时
    def dfs(self,preorder):
        # print(preorder)
        if len(preorder)==0:
            return True
        root=preorder[0]
        id=-1
        for i in range(len(preorder)):
            if preorder[i]>root:
                id=i####
                break########
        if id==-1:
            id=len(preorder)
        # print(id)

        flag=0
        for i in range(id,len(preorder)):
            if preorder[i]<root:
                flag=1
        if flag:
            return False

        return self.verifyPreorder(preorder[1:id]) and self.verifyPreorder(preorder[id:])

preorder =[1,3,4,2]
a=Solution()
print(a.verifyPreorder(preorder))