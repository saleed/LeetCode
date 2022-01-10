# -*- coding: utf-8 -*
"""

给你一个会议时间安排的数组 intervals ，每个会议时间都会包括开始和结束的时间 intervals[i] = [starti, endi] ，为避免会议冲突，同时要考虑充分利用会议室资源，请你计算至少需要多少间会议室，才能满足这些会议安排。

"""


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        startitv=sorted(intervals,key=lambda x:x[0])
        enditv=sorted(intervals,key=lambda x:x[1])

        num=0
        j=0
        maxnum=-float("inf")
        for v in startitv:
            if v[0]<enditv[j][1]:
                num+=1
            else:
                j+=1
            maxnum=max(maxnum,num)
        return maxnum


    ##最大堆比较好理解

