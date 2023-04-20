
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()

        minv=float("inf")

        for i in range(len(nums)):
            minv=min(minv,self.twosum(i+1,len(nums)-1,target-nums[i],nums))

        return minv




    def twosum(self,i,j,target,nums):
        minv=float("inf")
        while i<j:
            if nums[i]+nums[j]==target:
                return 0
            while i<j and  nums[i]+nums[j]<target:
                minv=min(minv,abs(target-(nums[i]+nums[j])))
                i+=1
            while i<j and nums[i]+nums[j]>target:
                minv = min(minv, abs(target -( nums[i] + nums[j])))
                j-=1

        return minv