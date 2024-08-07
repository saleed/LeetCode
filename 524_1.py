#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/29 09:35
# @Author  : sunaolin
# @File    : 524_1.py


class Solution(object):
    def findLongestWord(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: str
        """
        ##python怎么按照多key排序？？？？
        # 按照x长度反序列，x的字典序正序
        dictionary.sort(key=lambda x:(-len(x),x))

        # dictionary=dictionary[::-1]
        print(dictionary)


        for v in dictionary:
            if self.match(s,v):
                return v
        return ""

    def match(self,s,sub):
        p=0
        q=0
        while p<len(sub):
            while q<len(s) and s[q]!=sub[p]:
                q+=1
            if q==len(s):
                return False
            p+=1
            q+=1
        return True

s = "abpcplea"
dictionary = ["ale","bbbbb","apple","monkey","plea"]
a=Solution()
print(a.findLongestWord(s,dictionary))