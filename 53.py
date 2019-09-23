def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    #greed method:how to prove this method
    curmax=nums[0]
    cursum=nums[0]
    start=0
    end=1
    s=0
    t=1
    for i in range(1,len(nums)):
        if cursum+nums[i]<nums[i]:
            cursum=nums[i]
            start=i
            end=i+1
        else:
            cursum=cursum+nums[i]
            end=end+1
        if cursum>curmax:
            s=start
            t=end
            curmax=cursum
    return nums[s:t]





