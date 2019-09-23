def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums)==0:
        return []
    count=1
    pre=nums[0]
    id=1
    for i in nums[1:]:
        # print i,pre,count
        if i==pre and count==2:
            continue
        elif i==pre and count<2:
            nums[id]=i
            count=count+1
            id=id+1
        else:
            count=1
            nums[id]=i
            id=id+1
            pre=i
    # print id
    for i in range(len(nums)-id):
        nums.pop()
    return nums



tst= [1,1,1,2,2,3]

print removeDuplicates(tst)
tst=[0,0,1,1,1,1,2,3,3]
print removeDuplicates(tst)