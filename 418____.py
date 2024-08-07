#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/20 13:46
# @Author  : sunaolin
# @File    : 418.py


class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        r=0
        c=0
        cnt=0

        ##类似一个递推的问题 每次解决
        l=sum([len(v) for v in sentence])
        l+=len(sentence) ##计算用完一个sentence需要的空格数

        ##分两种情况，一行可以填满sentence 和填不满sentence 418的解法是以sentence为单位，看看一行能填满多少，填不满的再
        i=0
        while True:
            cnt+=int(cols/l)
            c+=int(cols/l)*l
            if c==cols:
                c=0
                r+=1
            else:
                ##利用周期性
                while c+len(sentence[i])<=cols:
                    c+=len(sentence[i])+1
                    i+=1
                    if i==len(sentence):
                        cnt+=1
                        i=0
                # print("11",c)
                c=0
                r+=1
            if r==rows:
                return cnt













sentence =["i","had","apple","pie"]
rows =4
cols=5
a=Solution()
print(a.wordsTyping(sentence,rows,cols))
