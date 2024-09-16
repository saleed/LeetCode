#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/9/16 11:06
# @Author  : sunaolin
# @File    : 858.py


##p,q的最小公倍数

"""
问题变得简单了，光线最终向上走的距离，其实就是 p 和 q 的最小公倍数。我们设最小公倍数为 L，会发现如果 L 是 p 的奇数倍，光线则到达北墙（可以参考上面的图）当 L 是 p 的 偶数倍，光线将会射到南墙。
问题来了，如果光线是射向南墙，因为只有一个接收器了，必定只能遇到接收器 0。但是如果射到了北墙，如何区分是 1 和 2。这回到了一个初中数学题，我们可以通过光线与东西墙的接触次数，来判断最终的落点是 1 还是 2。
"""

class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """

        mindiv=self.gcd(p,q)

        minmul=(p*q)/mindiv

        if (minmul/p)%2==0:
            return 0
        else:
            if (minmul/q)%2==1:
                return 1
            else:
                return 2

     ##辗转相除法
    def gcd(self,a,b):
        if a<b:
            a,b=b,a
        if a%b==0:
            return b
        return self.gcd(b,a%b)


