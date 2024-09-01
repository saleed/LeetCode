#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/7 19:22
# @Author  : sunaolin
# @File    : 678_1.py


class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ##思路错误，*并不是可以匹配任意位置的括号
        ##比如****((((无法匹配
        ##*必须出现在左括号右边或者右括号左边才可以匹配
        # st=0
        # star=0
        # for v in s:
        #     print(st,star)
        #     if v=="(":
        #         st+=1
        #     elif v==")":
        #         if st==0:
        #             if star>0:
        #                 star-=1
        #             else:
        #                 return False
        #         else:
        #             st-=1
        #     else:
        #         star+=1
        # return star>=st

        """
        括号匹配的问题可以用栈求解。
        如果字符串中没有星号，则只需要一个栈存储左括号，在从左到右遍历字符串的过程中检查括号是否匹配。
        在有星号的情况下，需要两个栈分别存储左括号和星号。从左到右遍历字符串，进行如下操作。
        如果遇到左括号，则将当前下标存入左括号栈。
        如果遇到星号，则将当前下标存入星号栈。
        如果遇到右括号，则需要有一个左括号或星号和右括号匹配，由于星号也可以看成右括号或者空字符串，因此当前的右括号应优先和左括号匹配，没有左括号时和星号匹配：
        如果左括号栈不为空，则从左括号栈弹出栈顶元素；
        如果左括号栈为空且星号栈不为空，则从星号栈弹出栈顶元素；
        如果左括号栈和星号栈都为空，则没有字符可以和当前的右括号匹配，返回false。
        遍历结束之后，左括号栈和星号栈可能还有元素。为了将每个左括号匹配，需要将星号看成右括号，且每个左括号必须出现在其匹配的星号之前。当两个栈都不为空时，每次从左括号栈和星号栈分别弹出栈顶元素，对应左括号下标和星号下标，判断是否可以匹配，匹配的条件是左括号下标小于星号下标，如果左括号下标大于星号下标则返回false。
        最终判断左括号栈是否为空。如果左括号栈为空，则左括号全部匹配完毕，剩下的星号都可以看成空字符串，此时s是有效的括号字符串，返回true。如果左括号栈不为空，则还有左括号无法匹配，此时s不是有效的括号字符串，返回false。
        """
        st=[]
        star=[]


        for i in range(len(s)):
            if s[i]=="(":
                st.append(i)
            elif s[i]=="*":
                star.append(i)
            else:
                if len(st):
                    st.pop()
                elif len(star):
                    star.pop()
                else:
                    return False

        if len(st)==0:
            return True

        if len(star)<len(st):
            return False

        print(st)
        print(star)

        p=len(st)-1
        q=len(star)-1
        while p>=0 and  q>=0:
            if star[q]>st[p]:
                q-=1
                p-=1
            else:
                return False
        return p==-1



