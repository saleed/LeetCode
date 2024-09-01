#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/29 10:44
# @Author  : sunaolin
# @File    : 831.py

class Solution(object):
    def maskPII(self, s):
        """
        :type s: str
        :rtype: str
        """

        if "@" in s:
            sp = s.split("@")
            if len(sp[0]) >= 2:
                return (sp[0][0] + "*" * 5 + sp[0][-1] + "@" + sp[1]).lower()
            else:
                return s.lower()
        else:
            news = ""
            for i in range(len(s)):
                if s[i].isdigit():
                    news += s[i]
            print(news)
            if len(news) == 10:
                return "***-***-" + news[-4:]
            if len(news) == 11:
                return "+*-***-***-" + news[-4:]
            if len(news) == 12:
                return "+**-***-***-" + news[-4:]
            if len(news) == 13:
                return "+***-***-***-" + news[-4:]
            return ""
