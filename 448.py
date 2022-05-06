class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        p=0
        res=[]
        while p<len(nums):
            q=p
            while nums[q]!=q+1:
                tmp=nums[nums[q]-1]
                nums[nums[q]-1]=nums[q]
                nums[q]=tmp
                if nums[q]==nums[nums[q]-1]:
                    break
            p+=1

        for i in range(len(nums)):
            if nums[i]!=i+1:
                res.append(i+1)
        return res

