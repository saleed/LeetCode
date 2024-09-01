#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/26 14:58
# @Author  : sunaolin
# @File    : 809.py


class Solution(object):
    def expressiveWords(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        cnt=0
        for v in words:
            if self.matchStr(v,s):
                print(v)
                cnt+=1
        return cnt





    def matchStr(self,w1,w2):
        p=0
        q=0
        while p<len(w1) and q<len(w2) and w1[p]==w2[q]:
            tmp=w1[p]
            pnum=0
            qnum=0
            while p<len(w1) and w1[p]==tmp:
                pnum+=1
                p+=1
            while q<len(w2) and w2[q]==tmp:
                qnum+=1
                q+=1
            # print(pnum,qnum,tmp)
            if (pnum<qnum and qnum>=3) or pnum==qnum: ##注意这个判定条件
                continue
            else:
                return False
        print(p,q)
        if p<len(w1) or q<len(w2):
            return False
        return True


