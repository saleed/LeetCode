def nextPermutation(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    if len(nums) == 0 or len(nums) == 1:
        return
    for i in list(reversed(range(len(nums) - 1))):
        if nums[i] < nums[i + 1]:
            break

    if i == 0 and nums[i] > nums[i + 1]:
        nums = list(reversed(nums))
        print nums
    else:
        for j in list(reversed(range(i + 1, len(nums)))):
            if nums[j] > nums[i]:
                break
        nums[i], nums[j] = nums[j], nums[i]
        nums = nums[:i + 1] + list(reversed(nums[i + 1:]))
        print nums



a=[1,3,2]
nextPermutation(a)
b=[3,2,1]
nextPermutation(b)
c=[1,3,6,5,2,1]
nextPermutation(c)





