#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/23 20:27
# @Author  : sunaolin
# @File    : 458_1.py


class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        n=int(minutesToTest/minutesToDie)

        bk=int(buckets/n)+1
        i=1
        while pow(2,i)<bk:
            i+=1
        return i