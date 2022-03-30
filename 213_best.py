class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        dpRob0=[0]*len(nums)
        dpNotRob0=[0]*len(nums)

        dpRob0[0]=nums[0]
        dpRob0[1]=0 #####
        for i in range(2,len(nums)-1):
            for j in range(i-1):
                dpRob0[i]=max(dpRob0[i],nums[i]+dpRob0[i])
        rob0=max(dpRob0)

        dpNotRob0[0]=0
        dpNotRob0[1]=nums[1]
        for i in range(2,len(nums)):
            for j in range(i-1):
                dpNotRob0[i]=max(dpNotRob0[i],nums[i]+dpNotRob0[i])
        notrob0=max(dpNotRob0)

        print(rob0,notrob0)

        return max(rob0,notrob0)


