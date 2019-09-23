def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    maxh=0
    maxid=0
    for i in range(len(height)):
        if height[i]>maxh:
            maxh=height[i]
            maxid=i
    root=0
    area=0
    for i in range(0,maxid):
        if height[i]>height[root]:
            root=i
        else:
            area += height[root] - height[i]

    root=len(height)-1
    for i in list(reversed(range(maxid,len(height)))):
        if height[i]>height[root]:
            root=i
        else:
            area+=height[root]-height[i]
    return area

test=[0,1,0,2,1,0,1,3,2,1,2,1]
print trap(test)
