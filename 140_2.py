#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/1 12:36
# @Author  : sunaolin
# @File    : 140_2.py


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        dp=[ [] for _ in range((len(s)+1))]
        dp[0].append(-1)
        for i in range(1,len(s)+1):
            for j in range(i):
                if len(dp[j])>0 and s[j:i] in wordDict:
                    dp[i].append(j)

            # print(i,dp[i])

        res=[]
        print("####",len(dp)-1)
        self.trackBack(dp,len(dp)-1,s,[],res)
        return res


    def trackBack(self,dp,i,s,tmp,res):
        # print(i,tmp)
        if i==0:
            res.append(" ".join(tmp[::-1]))
            return
        for j in range(len(dp[i])):
            tmp.append(s[dp[i][j]:i])
            self.trackBack(dp,dp[i][j],s,tmp,res)
            tmp.pop()



a="catsanddog"
wordDict =["cat","cats","and","sand","dog"]

test=Solution()
test.wordBreak(a,wordDict)