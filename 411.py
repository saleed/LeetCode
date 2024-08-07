#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/18 22:51
# @Author  : sunaolin
# @File    : 411.py

class Solution(object):
    def minAbbreviation(self, target, dictionary):
        """
        :type target: str
        :type dictionary: List[str]
        :rtype: str
        """

        res1=[]
        self.dfs(target,0,0,dictionary,"",res1)
        res2=[]
        self.dfs(target,0,1,dictionary,"",res2)
        res=res1+res2
        res.sort(key=lambda x:len(x))
        for v in res:
            flag=1
            for d in dictionary:
                if self.match(d,v):
                    flag=0
            if flag:
                return v



    def dfs(self,word,i,flag,dic,tmp,res):
        # print(res)
        if i==len(word):
            # for v in dic:
            #     print(tmp,v)
            #     if self.match(v,tmp):
            #         return False
            # res[0]=tmp[:]
            res.append(tmp[:])
            return True
        if i<len(word):
            if flag == 0:
                for j in range(i,len(word))[::-1]:
                    newtmp=tmp+str(len(word[i:j+1]))
                    self.dfs(word,j+1,1,dic,newtmp,res)
            else:
                for j in range(i,len(word)):
                    newtmp=tmp+word[i:j+1]
                    self.dfs(word,j+1,0,dic,newtmp,res)

        return False

    def match(self,word,sub):
        i=0
        ptr=0
        while i<len(sub) and ptr<len(word):
            while i<len(sub) and sub[i].isalpha():
                if ptr>=len(word) or word[ptr]!=sub[i]:
                    return False
                i+=1
                ptr+=1
            tmp=""
            while i<len(sub) and sub[i].isdigit():
                tmp+=sub[i]
                i+=1
            if tmp!="":
                # print("tmp",tmp)
                ptr+=int(tmp)
        return ptr==len(word) and i==len(sub)

a=Solution()
print(a.match("apple","5"))
target ="apple"
dictionary =["blade"]
# print(se.match(""))
print(a.minAbbreviation(target,dictionary))

