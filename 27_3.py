#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/16 15:52
# @Author  : sunaolin
# @File    : 27_3.py

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/16 15:50
# @Author  : sunaolin
# @File    : 26_3.py

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre=float("inf")
        p=0
        for i in range(len(nums)):
            if nums[i]!=pre:
                nums[p]=nums[i]
                p+=1
                pre=nums[i]
        return p+1