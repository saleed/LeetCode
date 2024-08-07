#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/20 14:10
# @Author  : sunaolin
# @File    : 418_1.py

class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        p = 0
        r = 0
        c = 0
        cnt = 0
        l = sum([len(i) for i in sentence])
        l += len(sentence)
        print(l)

        while r < rows:
            # print("xxx",cols,c,l)
            if cols - c >= l:
                cnt += int((cols - 1 - c) / l)
                c += l * int((cols - 1 - c) / l)
            # print(r,c,cnt,p)
            if c + len(sentence[p]) > cols:
                r += 1
                c = 0
            else:
                if c + len(sentence[p]) == cols:
                    c = 0
                    r += 1
                else:
                    c += len(sentence[p]) + 1
                p += 1
                # print(p)
                if p == len(sentence):
                    # print(11)
                    cnt += 1
                    p = 0
        return cnt

