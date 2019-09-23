# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if len(intervals)==0:
            return newInterval
        id=-1
        state=-1

        for i in intervals:
            if newInterval.start >intervals[i].start:
                continue
            else:
                id=i
                break


        right=id-1
        if newInterval.start<intervals[id].end:
            for j in range(id-1,len(intervals)):
                if newInterval.end<=intervals[j].end and newInterval.end>=intervals[j].start:
                    right=j
                elif newInterval.end>intervals[j].end and newInterval.







        else:




