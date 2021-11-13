class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ##丢数，选取pair如果两个不一样，就丢弃，相同就保留


        if len(nums)==0:
            return
        p=0
        q=0
        while q<len(nums):
            if nums[q]==nums[p]:
                q+=1
            else:
                nums[p]=float("inf")
                nums[q]=float("inf")
                p+=1
                q+=1
        while p<len(nums):
            if nums[p]!=float("inf"):
                return nums[p]
            p+=1

