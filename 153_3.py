class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p=0
        q=len(nums)-1
        if len(nums)==1:
            return nums[0]
        while p<=q:
            mid=int((p+q)/2)
            if mid>0 and mid<len(nums)-1:
                if nums[mid]<nums[mid+1]and nums[mid]<nums[mid-1]:
                    return nums[mid]
                if nums[mid]>nums[mid+1] and nums[mid]>nums[mid-1]:
                    return nums[mid+1]
            if mid==0:
                if nums[1]>nums[0]:
                    return nums[0]
                else:
                    return nums[1]

            #左右两边有可能都是有序的
            #优先判断右半边，假如在整个数组有序的情况下，右半边的数据一定优先淘汰掉
            if nums[mid]<nums[q]:
                q=mid
            else:
                p=mid+1
        return float("inf")


a=Solution()
print(a.findMin([6,1,2,3,5]))