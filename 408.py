#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/18 16:47
# @Author  : sunaolin
# @File    : 408.py


class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        if len(word) == 0:
            return True
        if word[0].isdigit():
            flag = False
        else:
            flag = True

        i = 0
        res = 0
        while i < len(abbr):
            if flag == False:
                tmp = ""
                while i < len(abbr) and abbr[i].isdigit():
                    tmp += abbr[i]
                    i += 1
                if len(tmp) == 0:
                    return False
                if tmp.startswith("0"):
                    return False
                res += int(tmp)
            else:
                while i < len(abbr) and res<len(word) and word[res]==abbr[i]:
                    i += 1
                    res+=1
            flag = not flag
        return res == len(word)




