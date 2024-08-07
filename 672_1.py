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


        if presses==1:




    def dfs(self,):