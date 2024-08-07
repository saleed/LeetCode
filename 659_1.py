#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/6 16:29
# @Author  : sunaolin
# @File    : 659_1.py

import collections,heapq
class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        predict = collections.defaultdict(list) ##这里创建一个字典 和{}字典相比，不会有key为空的奉献

        for v in nums:
            print(v, predict)
            try:
                if v-1 in predict and len(predict[v-1])>0:
                    l=heapq.heappop(predict[v-1])
                    heapq.heappush(predict[v],l+1)
                else:
                    heapq.heappush(predict[v],1)
            except:
                print(v,predict)


        return not any(queue and queue[0] < 3 for queue in predict.values())


nums =[1,2,3,3,4,5]

a=Solution()
print(a.isPossible(nums))


