#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/7 20:04
# @Author  : sunaolin
# @File    : 680_1.py
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        mid=0

        ##从中间将s分成两段，分删除的字符在左侧还是右侧两部分考虑，确定中间位置
        if len(s)%2==0:
            mid=len(s)/2-1
            if self.check(s,mid+1,mid+1) or self.check(s,mid,mid):
                return True
            return False

        else:
            mid=len(s)/2
            if self.check(s,mid,mid+1) or self.check(s,mid,mid-1):
                return True
            return False




        ###


    def check(self,s,p,q):
        cnt=0
        while not (p==-1 or q==len(s)):
            if s[p]==s[q]:
                p-=1
                q+=1
            else:
                cnt+=1
                if len(s)-1-q+1>p+1:
                    q+=1
                else:
                    p-=1
            if cnt>1:
                return False
        return True

