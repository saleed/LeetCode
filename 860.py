#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/9/16 22:07
# @Author  : sunaolin
# @File    : 860.py


class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """

        change={}
        change[5]=0
        change[10]=0
        change[20]=0


        for v in bills:
            if v%5!=0:
                return False
            if v==5:
                change[5] += 1
            elif v==10:
                if change[5]>0:
                    change[5]-=1
                    change[10]+=1
                else:
                    return False
            elif v==20:
                if change[10]>0 and change[5]>0:
                    change[10]-=1
                    change[5]-=1
                elif change[5]>2:
                    change[5]-=3
                else:
                    return False
        return True


