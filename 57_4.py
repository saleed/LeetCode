class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        res = []
        flag = 0
        i = 0
        intervals.append([float("inf"), float("inf")])
        while i < len(intervals) and newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
            i += 1
        left = min(intervals[i][0], newInterval[0])
        while i < len(intervals) and newInterval[1] >= intervals[i][1]:
            i += 1
        if intervals[i][0] > newInterval[1]:
            right = newInterval[1]
        else:
            right = intervals[i][1]
            i += 1  ##合并区间
        res.append([left, right])
        res += intervals[i:]
        return res[:-1]



