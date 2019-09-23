def insert( intervals, newInterval):
    """
    :type intervals: List[Interval]
    :type newInterval: Interval
    :rtype: List[Interval]
    """
    #这种方法相对来说比较耗时，消耗了多余的操作
    out=[]
    intervals.append(newInterval)
    for i in sorted(intervals, key=lambda i: i[0]):
        if out and i[0] <= out[-1][1]:
            out[-1][1] = max(out[-1][1], i[1])
        else:
            out += i,
    return out



    #分析直接插入的方法：
    #首先对既有区间按左边界排序
    #然后考虑新区间的左边界，加入左边界落入一个区间内，