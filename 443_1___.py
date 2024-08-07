#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/22 16:14
# @Author  : sunaolin
# @File    : 443——1.py


class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars)==0:
            return 0

        chars.append("-1")
        pre=chars[0]
        p=1
        i=1
        cnt=1
        while i<len(chars):
            if chars[i]==pre:
                cnt+=1
            else:
                if cnt>1:
                    strcnt=""
                    while cnt:
                        strcnt+=str(cnt%10)
                        cnt=int(cnt/10)
                    for v in strcnt[::-1]:
                        chars[p]=v
                        p+=1
                chars[p]=chars[i]
                p+=1
                cnt=1
                pre=chars[i]
            i+=1
        return p-1

