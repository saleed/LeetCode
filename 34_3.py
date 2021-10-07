class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return self.binarySearch(nums,target)



    def binarySearch(self,nums,target):
        p=0
        q=len(nums)-1
        leftbound=float("inf")

        while p<=q:
            mid=(p+q)/2
            if nums[mid]==target:
                leftbound=min(leftbound,mid)
                q=mid-1
            elif nums[mid]<target:
                p=mid+1
            else:
                q=mid-1

        p = 0
        q = len(nums) - 1
        rightbound = -float("inf")

        while p <= q:
            mid = (p + q) / 2
            if nums[mid] == target:
                rightbound = max(rightbound, mid)
                p=mid  +1
            elif nums[mid] < target:
                p = mid + 1
            else:
                q = mid-1   ##因为这里携程q=mid导致死循环，最好是写成q=mid-1

        if rightbound<leftbound:
            return [-1,-1]
        return [leftbound,rightbound]










    def iterSearch(self,nums,target):
        minv=float("inf")
        maxv=-float("inf")
        for i in range(len(nums)):
            if nums[i]==target:
                minv=min(minv,i)
                maxv=max(maxv,i)
        if minv==float("inf") and maxv==-float("inf"):
            return [-1,-1]
        return [minv,maxv]