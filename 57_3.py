class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        res=[]

        #思路其实就是状态切换
        intervals.append([float("inf"),float("inf")])  ###注意细节，这里需要先append一个边界否则，否则当n
        ####这个太重要了，状态机！！！！！

        status=0
        if len(intervals)==0:
            return [newInterval]
        left=-1
        right=-1
        i=0

        ## 能用while 就不要用for  for虽然简洁，但是对索引下标没有好的控制

        while i<len(intervals):
            intv=intervals[i]
            if status==0:
                if newInterval[0]>intv[1]:
                    res.append(intv)
                    i += 1
                else:
                    left=min(newInterval[0],intv[0])
                    status=1
            elif status==1:
                if newInterval[1]>intv[1]:
                    i+=1
                    continue
                elif newInterval[1]<intv[0]:
                    right=newInterval[1]
                    res.append([left,right])
                else:
                    right=max(intv[1],newInterval[1])
                    res.append([left,right])
                    i+=1
                status=2
            else:
                res.append(intv)
                i+=1

        return res[:-1]


