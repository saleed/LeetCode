class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """


        p=0
        q=len(nums)-1
        while p<=q:
            mid=(p+q)/2
            if nums[mid]==target:
                return True
            if nums[p]==nums[mid]:#####主要就在于这里，如果遇到mid和p相同，怎么继续更新边界
                p+=1
            elif nums[p]<nums[mid]:
                if nums[p]<=target<nums[mid]:
                    q=mid-1
                else:
                    p=mid+1
            else:
                if nums[mid]<target<=nums[q]:
                    p=mid+1
                else:
                    q=mid-1
        return False


