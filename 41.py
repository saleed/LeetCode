def firstMissingPositive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    ##
    for i in range(len(nums)):
        j=i
        while nums[j] < len(nums) and nums[j] > 0 and nums[nums[j]-1] != nums[j]:
            print j ,nums[j]
            tmp=nums[nums[j]-1]
            nums[nums[j]-1]=nums[i]
            nums[j]=tmp
             ###############very special process,see test2
            print "TT",nums
    print nums
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return i + 1
    return len(nums)+1



test1=[1,2,0]
print firstMissingPositive(test1)
test2=[-1,4,2,1,9,10]
print firstMissingPositive(test2)