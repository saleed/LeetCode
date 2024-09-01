#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/13 16:06
# @Author  : sunaolin
# @File    : 722_1.py


class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """

        strsource="\n".join(source)

        res=""
        i=0
        while i<len(strsource):
            if i+1<len(strsource) and strsource[i:i+2]=="//":
                i+=2
                while i<len(strsource) and strsource[i]!="\n":
                    i+=1
            elif i+1<len(strsource) and strsource[i:i+2]=="/*":
                i+=2  ##这里要注意 /*/也为合法的注释开头
                while i+1<len(strsource) and strsource[i:i+2]!="*/":
                    i+=1
                i+=2
            else:
                res+=strsource[i]
                i+=1

        print(strsource)
        print(res)

        res=res.split("\n")
        while  ""  in res:  ##移除空字符
            res.remove("")
        return res



