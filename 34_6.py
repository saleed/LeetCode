#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/16 19:16
# @Author  : sunaolin
# @File    : 34_6.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/16 19:16
# @Author  : sunaolin
# @File    : 34_6.py


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        p=0
        q=len(nums)-1
        while p<q:
            # print(p,q)
            mid=int((p+q)/2)
            print(mid)
            if nums[mid]==target:
                q=mid
            elif nums[mid]<target:
                p=mid+1
            else:
                q=mid
        left=-1
        if target==nums[p]:
            left=p
        p=0
        q=len(nums)-1
        while p<q:
            mid=int((p+q)/2+1)####????为什么要加强制类型转换
            if nums[mid]==target:
                p=mid
            elif nums[mid]<target:
                p=mid
            else:
                q=mid-1
        right=-1
        if nums[p]==target:
            right=p
        return [left,right]


a=Solution()
test=[5,7,7,8,8,10]
print(a.searchRange(test,6))