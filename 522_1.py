#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/28 18:16
# @Author  : sunaolin
# @File    : 522_1.py

class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        vdict={}
        for v in strs:
            if len(v) in vdict:
                vdict[len(v)].append(v)
            else:
                vdict[len(v)]=[v]


        ks=vdict.keys()
        ks.sort()
        ks=ks[::-1]
        print(vdict)

        leftstr=[]
        for i in range(len(ks)):
            same,ret= self.checkSame(vdict[ks[i]])
            print(same,ret,leftstr)
            if same==False:
                if i > 0:
                    for s in ret:
                        flag=0
                        for v in leftstr:
                            if self.checkSubStr(v, s):
                                flag=1
                                break
                        if not flag:
                            return len(s)

                else:
                    return len(ret[0])
            else:
                leftstr.extend(ret)
        return -1



    def checkSame(self,strs):
        if len(strs)==0:
            return True,[]

        vdict={}

        for s in strs:
            if s in vdict:
                vdict[s]+=1
            else:
                vdict[s]=1
        res = []
        res1=[]
        for k in vdict:
            if vdict[k]==1:
                res1.append(k)
            else:
                res.append(k)
        if len(res1)>0:
            return False,res1
        return True,res
    def checkSubStr(self,a,b):

        p=0
        q=0
        while q<len(b):
            while p<len(a) and a[p]!=b[q]:
                p+=1
            if p==len(a):
                return False
            else:
                p+= 1
                q+=1
        return True
a=Solution()
print(a.checkSubStr("eaec","eae"))