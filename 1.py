
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        if target-nums[i] in nums[i+1:]:
            return i,i+1+nums[i+1:].index(target-nums[i])


# test slice
a=[1,2,3,5,6]

b=a[1:]
print b
for itm in a[1:]:
    print itm


nums1=[2, 7, 11, 15]
nums2=[3,2,4]
print twoSum(nums1,9)
print twoSum(nums2,6)
