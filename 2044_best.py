class Solution(object):
    def countMaxOrSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res=1

        for i in range(32):
            flag=0
            for j in range(len(nums)):
                if nums[j]/pow(2,i)%2==1:
                    flag+=1
            if flag==0:
                flag=len(nums)
            res*=flag
        return min(res)