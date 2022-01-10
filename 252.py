# -*- coding: utf-8 -*
"""

给定一个会议时间安排的数组 intervals ，每个会议时间都会包括开始和结束的时间 intervals[i] = [starti, endi] ，请你判断一个人是否能够参加这里面的全部会议。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/meeting-rooms
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""



class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        intervals=sorted(intervals,key=lambda x:x[0])
        print(intervals)
        for i in range(1,len(intervals)):
            if intervals[i][0]>intervals[i-1][1]:
                continue
            else:
                return False
        return True

a=Solution()
print(a.canAttendMeetings([[7,10],[2,4]]))


