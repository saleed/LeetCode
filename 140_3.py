#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/10/7 22:26
# @Author  : sunaolin
# @File    : 140_3.py



class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        dp=[ [] for _ in range((len(s)+1))]
        dp[0].append(-1)##增加标志，
        for i in range(len(s)):
            for j in range(i+1):
                if s[j:i+1] in wordDict and len(dp[j])>0:
                    dp[i+1].append(j) ##这里的i是s下标+1  j是下标，物理意义不同，backt
        print(dp)
        res=[]
        self.backTrack(dp,res,s,len(dp)-1,[])
        return res


    def backTrack(self,dp,res,s,i,tmp):
        if i==0:
            res.append(" ".join(tmp[::-1]))
            return
        for j in dp[i]:
            tmp.append(s[j:i]) ##i是下标+1,
            self.backTrack(dp,res,s,j,tmp)##这里对应的是下标为j-1的s那个字符，存在dp[j]上
            tmp.pop()

