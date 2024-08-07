#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/11 17:35
# @Author  : sunaolin
# @File    : 301——1.py

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        st=0
        rnum=0
        for i in range(len(s)):
            if s[i]=="(":
                st+=1
            elif s[i]==")":
                if st==0:
                    rnum+=1
                else:
                    st-=1
        lnum=st

        res=[]
        print(lnum,rnum)
        self.dfs(s,0,lnum,rnum,0,[],res)
        print(res)
        return res




    def dfs(self,s,i,lnum,rnum,st,tmp,res):
        # print(s,i,lnum,rnum,st,tmp)
        if i==len(s) and lnum==0 and rnum==0 and st==0:
            if "".join(tmp[:]) not in res:
                res.append("".join(tmp[:]))
            return
        elif i<len(s):
            if s[i]=="(":
                if lnum>0:
                    self.dfs(s,i+1,lnum-1,rnum,st,tmp,res)
                tmp.append("(")
                self.dfs(s,i+1,lnum,rnum,st+1,tmp,res)
                tmp.pop()
            elif s[i]==")":
                if rnum>0:
                    self.dfs(s,i+1,lnum,rnum-1,st,tmp,res)
                if st>0:
                    tmp.append(")")
                    self.dfs(s,i+1,lnum,rnum,st-1,tmp,res)
                    tmp.pop()
            else:
                self.dfs(s,i+1,lnum,rnum,st,tmp+[s[i]],res)




