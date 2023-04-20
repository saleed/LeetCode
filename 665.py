class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        nums=[-float("inf")]+nums+[float("inf")]
        cnt=0
        for i in range(2,len(nums)):
            if nums[i]<nums[i-1]:
                if nums[i]>nums[i-2]:
                    nums[i-1]=nums[i-2]
                else:
                    nums[i]=nums[i-1]
                cnt+=1
                if cnt>1:
                    return False
        return True