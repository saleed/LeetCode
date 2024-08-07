#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/17 16:53
# @Author  : sunaolin
# @File    : 388_1.py


class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        input=input+"\n\t"

        i=0
        st=[]
        maxl=0
        while i<len(input):
            print(i)
            tmp=""
            while i<len(input) and (input[i]!="\n"):
                tmp+=input[i]
                i+=1
            st.append(len(tmp))
            if "." in st[-1]:
                maxl=max(maxl,sum(st)+len(st)-1)

            ntlen=0
            i+=1
            while i<len(input) and input[i]=="\t":
                ntlen+=1
                i+=1

            while ntlen<len(st):
                st.pop()

            print("xxx",i,len(input))


        return maxl
a=Solution()
test="dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
a.lengthLongestPath(test)



