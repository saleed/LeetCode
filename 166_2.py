#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/4 13:04
# @Author  : sunaolin
# @File    : 165_1.py
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        prefix=""
        if numerator*denominator<0:
            prefix="-"
        numerator=abs(numerator)
        denominator=abs(denominator)

        div=int(numerator/denominator)
        res=str(div)
        left=numerator%denominator
        if left==0:
            return prefix+res
        else:
            res+="."

        visdict={}
        while left:
            if left in visdict:
                id=visdict[left]
                res=res[:id]+"("+res[id:]+')'
                return prefix+res
            else:
                tmp=""
                visdict[left]=len(res)
                left*=10
                while left<denominator:
                    tmp+="0"
                    left*=10
                print(left,denominator)
                tmp+=str(int(left/denominator))
                print(res)
                left=left%denominator
                res+=tmp

        return prefix+res

numerator =-1
denominator =-2147483648
a=Solution()
print(a.fractionToDecimal(numerator,denominator))

print(1/2147483648)