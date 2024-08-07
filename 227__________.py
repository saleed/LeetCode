#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/7 18:57
# @Author  : sunaolin
# @File    : 227_1.py

# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/7 17:58
# @Author  : sunaolin
# @File    : 227.py


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        st=[]
        start=0
        for i in range(len(s)):
            if s[i] in ("*", "/"):




    def calcu(self, a, op, b):
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        else:
            return int(a / b)
