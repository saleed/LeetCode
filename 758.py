#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/18 11:18
# @Author  : sunaolin
# @File    : 758_1.py


class Solution(object):
    def boldWords(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: str
        """

        i=0
        res=""
        words.sort(key=lambda x:len(x))
        words=words[::-1]

        ##太难想了，
        print(words)
        while i<len(s):
            j=i
            end=i
            while True:
                for v in words:
                    if j+len(v)<=end:
                        break
                    if s[j:j+len(v)]==v:
                        end=j+len(v)
                j+=1
                if j>end:
                    break
            print(i,end)
            if i!=end:
                res+="<b>"+s[i:end]+"</b>"
                i=end
            else:
                res+=s[i]
                i+=1

        return res

