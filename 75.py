def sortColors(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    a=[0]*3
    for i in nums:
        a[i]=a[i]+1
    i=0
    for j in range(3):
        for t in range(a[j]):
            nums[i]=j
            i=i+1



a=[0]*3
a[1]=2
print a

color= [2,0,2,1,1,0]
print sortColors(color)
