#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/10/4 19:35
# @Author  : sunaolin
# @File    : 134_3.py


class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        i=0
        while i<len(gas):
            cnt=0
            j=i
            agg=0

            while cnt<len(gas):
                agg+=(gas[j]-cost[j])
                # print("agg",j,agg)
                if agg>=0: ###是大于等于0
                    cnt+=1
                    j=(j+1)%len(gas)
                else:
                    if j>=i: ##必须是大于等于i
                        i=j+1
                    else:
                        i=len(gas)
                    break
            if cnt==len(gas):
                return i
            # print(i,cnt)
        return -1
